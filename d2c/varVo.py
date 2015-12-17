#!/bin/python
# coding=utf-8


def getValueWrap(value, type):
    # 返回属性值的包装
    if 'string' == type:
        # 转义 " 到 \"
        return '"%s"' % (value.replace('"', r'\"'))
    elif 'lstring' == type:
        return '[[%s]]' % value
    elif 'int' == type:
        return int(value)
    elif 'float' == type:
        return number(value)
    elif 'json' == type:
        return value
    elif 'bool' == type:
        return 'true' if value == 'true' or value == '1' else 'false'
    print value



# string      name             // 文件名 xxx.csv
# string      trimmedName      // 文件名 xxx
# string      fileName         // 文件名 d:/xxx.csv
# <RowData>   data             // 数据
class CSVVo:
    def __init__(self, fileName, rows):
        self.data = data
        self.setFileName(fileName)
        self.rows = rows

    def setFileName(self, fileName):
        self.fileName = fileName
        idx = max(fileName.rfind('/'), fileName.rfind('\\'))
        self.name = fileName if -1 == idx else fileName[idx+1:]
        idx = self.name.rfind('.')
        self.trimmedName = self.name if -1 == idx else self.name[:idx]


# 模板信息
class TemplateInfo:
    def __init__(self, name = None, outputName = None):
        self.name = name                # string 模板名
        self.outputName = outputName    # string 导出文件名
        self._template = None           # Template 模板

class ManageVo:
    def __init__(self):
        self.templates = None           # <TemplateInfo> 模板信息
        self.clsTemplates = None        # <TemplateInfo> 类的默认模板
        self.classes = []               # <Class> 

# string      name            // 属性名
# string      value           // 属性值
# string      type            // 属性类型
class VarVo:
    def __init__(self):
        self.type = None                       # string 属性类型
        self.name = None                       # string 属性名
        self.value = None                      # string 属性值
        self.defaultValue = None               # string 默认值
        self.isDel = False                     # bool   是否已删除
        self.isPercent = False                 # bool   是否百分比

    def clone(self):
        var = VarVo()
        var.type = self.type
        var.name = self.name
        var.value = self.value
        var.defaultValue = self.defaultValue
        var.isDel = self.isDel
        var.isPercent = self.isPercent
        return var

    def __str__(self):
        return "[VarVo name:%s]" % (self.name)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, name):
        if 'valuew' == name:
            return getValueWrap(self.value, self.type)
        # print "__getitem__", name, name in self.__dict__
        return self.__dict__[name]

    def __getattr__(self, name):
        # print "__getattr__", name, name in self.__dict__
        return self.__getitem__(name)



# 表示csv里的一行数据
# 模板变量 rows<RowData> 数组
# 模板变量 rowmap<rowKey, RowData> 
class RowData:
    def __init__(self, cls):
        self._class = cls                       # ClassVo 对应的类
        self.indexNames = cls.indexNames        # <string> 索引属性名列表   (仅当是map形式的时候)
        self.indexVars = []                     # <Var> 索引属性变量列表   (仅当是map形式的时候)
        self.originVars   = []                  # <VarVo> 原始的属性列表 等同于 class.vars var.type 有效
        self.vars  = []                         # <VarVo> 过滤掉删除的属性列表，类似于originVars


    def getClass(self):
        # 返回该数据对应的类
        return self._class

    # def __getitem__(self, key):
    #     if key == 'class':
    #         return self._class
    #     raise KeyError("RowData instance has no attribute '%s'" % (key))






# CSV         csv              // 对应的csv
# <string>    templates        // 对应的模板名
# string      name             // 类名
# <string>    indexNames       // 索引属性名列表
# <int>       indexs           // 索引值
# bool        isMap            // 是否索引为key
# <Var>       vars             // 属性列表
class ClassVo:
    def __init__(self):
        self.csv = None                         # CSVVo  csv
        self.csvName = None                     # string csv名字
        self.templates = None                   # <TemplateInfo> 模板
        self.name = None                        # string 类名
        self.isMap = False                      # bool   该类是否为key/value形式
        self.indexNames = []                    # <string> 索引属性名列表
        self.indexs = []                        # <int> 引属性值列表(不包含被删除的)
        self.vars = []                          # <VarVo> 变量列表(不包含被删除的)
        self.originIndexs = []                  # <int> 原始的引属性值列表(包含被删除的)
        self.originVars = []                    # <VarVo> 原始变量列表

    # def getIndexs(self):
    #     return self._indexs

    # def getVars(self):
    #     return self._vars

