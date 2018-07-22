#!/bin/python
# coding=utf-8

import re

from ..function import indexOfKey
from ..varVo import TemplateInfo, ManageVo, ClassVo, VarVo


P_INDEXS = r'index\((.*)\)'  # index()
P_TEMPLATES = r'template\((.*)\)'  # template()
P_CLS_TEMPLATES = r'clsTemplate\((.*)\)'  # clsTemplate()
P_WHITESPACE = r'\s+'  # 空白
P_COMMA_SPACE = r'\s*,\s*'  # 逗号


# remove comment
def removeComment(s):
    # '#' or '//' is comment
    l = len(s)
    idx1 = s.find('#')
    idx1 = idx1 if idx1 != -1 else l
    idx2 = s.find('//')
    idx2 = idx2 if idx2 != -1 else l

    idx = min(idx1, idx2)
    if idx != l:
        return s[:idx]
    return s


# return <string> or None(没有匹配)
# 读取模式列表
def readPatternList(s, pattern):
    s = removeComment(s).strip()
    res = re.search(pattern, s)
    if res is None:
        return None
    s = res.group(1).strip()
    if len(s) == 0:
        return []
    return re.split(P_COMMA_SPACE, s)


# return <TempleteInfo> or None(没有匹配)
# 读取模板列表
def readTempleteInfoList(s, pattern):
    arr = readPatternList(s, pattern)
    if arr is not None:
        arr = [TemplateInfo(*x.split('|')) for x in arr]

    return arr


class ManageParser:
    def parse(self, s):
        mng = ManageVo()

        s = s.strip()
        lines = re.split('\r\n|\n', s)
        for line in lines:
            line = removeComment(line).strip()
            if len(line) > 0:
                arr = readTempleteInfoList(line, P_TEMPLATES)
                if arr is not None:
                    mng.templates = arr
                else:
                    arr = readTempleteInfoList(line, P_CLS_TEMPLATES)
                    mng.clsTemplates = arr

        if mng.templates is None or len(mng.templates) == 0:
            raise NameError('can not found template in manage')

        return mng


class ClassParser:
    def parse(self, s, manage):
        # return ClassVo
        cls = ClassVo()
        s = s.strip()
        arr = re.split('\r\n|\n', s)
        lines = []
        for line in arr:
            line = removeComment(line).strip()
            if len(line) > 0:
                lines.append(line)

        idx = 0
        # className and csvname
        self.readClsCsvName(lines[0], cls)
        # read template
        idx = idx + self.readTemplates(lines[1], cls)
        # read indexs
        idx = idx + 1
        self.readIndexs(lines[idx], cls)
        hasRepeat = False
        for line in lines[idx + 1:]:
            vo = self.readVar(line, cls)
            if hasRepeat and vo.isRepeat:
                raise NameError('repeat must at last var')
            if vo.isRepeat:
                hasRepeat = True

        self.setIndexs(cls)

        manage.classes.append(cls)

    def readClsCsvName(self, s, cls):
        # read class name and csv name
        names = re.split(P_WHITESPACE, s)
        if len(names) != 2:
            raise NameError('class first line not two name:' + s)

        cls.name = names[0].strip()
        cls.csvName = names[1].strip()

    def readTemplates(self, s, cls):
        cls.templates = readTempleteInfoList(s, P_TEMPLATES)
        return cls.templates is not None

    def readIndexs(self, s, cls):
        arr = readPatternList(s, P_INDEXS)
        if arr is None:
            raise NameError('can not found index(...)')
        if len(arr) > 0:
            cls.isMap = True
            cls.indexNames = arr
        else:
            P_CLS_TEMPLATES

    def readVar(self, s, cls) -> VarVo:
        s = removeComment(s).strip()
        if len(s) == 0:
            return None
        arr = re.split(P_WHITESPACE, s)
        l = len(arr)
        if l != 2 and l != 4:
            raise NameError('var format error: ' + s)
        elif l == 4 and arr[2] != '=':
            raise NameError('var format error: ' + s)

        vo = VarVo()
        vo.name = arr[1]
        vo.defaultValue = arr[3] if l == 4 else None
        res = re.search(r'([\-%*]*)(\S+)', arr[0])
        vo.type = res.group(2)
        addition = res.group(1)
        vo.isDel = addition.find('-') != -1
        vo.isPercent = addition.find('%') != -1
        vo.isRepeat = addition.find('*') != -1
        cls.originVars.append(vo)
        return vo

    def setIndexs(self, cls):
        if not cls.isMap:
            return
        # print 'names', cls.indexNames
        # print 'vars', cls.vars

        # 设置未被删除的变量列表
        for var in cls.originVars:
            if not var.isDel:
                cls.vars.append(var)

        # 设置indexs
        for name in cls.indexNames:
            # print '---------', name
            idx = indexOfKey(cls.originVars, name, 'name')
            if idx < 0:
                raise NameError('can not found index name: %s in %s' %
                                (name, cls.name))
            cls.originIndexs.append(idx)

            idx = indexOfKey(cls.vars, name, 'name')
            if idx < 0:
                raise NameError('index name [%s] was deleted in %s' %
                                (name, cls.name))
            cls.indexs.append(idx)


# 类定义解析器
class DefParser:
    def __init__(self):
        self.data = None  # string 元素数据
        self.manage = None  # ManageVo

    def parse(self, s):
        parts = re.split('^-{5,}$', s, flags=re.MULTILINE)
        if len(parts) == 1:
            self.parseManage('')
            self.parseClasses(parts[0])
        elif len(parts) == 2:
            self.parseManage(parts[0])
            self.parseClasses(parts[1])
        else:
            raise NameError('has more -----')

    def parseManage(self, s):
        self.manage = ManageParser().parse(s)

    def parseClasses(self, s):
        s = s.strip()
        blocks = re.split('\r\n\r\n+|\n\n+', s)
        for block in blocks:
            if block:
                ClassParser().parse(block, self.manage)


d = '''template:template.txt template.txt2
classTemplate:class.txt

1
------------------------------------------
2
UserShopStaticVo shop.csv
template(template.txt)
index(id,frushTime)
int id
json frushTime
int limitLevel
'''

# parser = DefParser()
# parser.parse(d)
