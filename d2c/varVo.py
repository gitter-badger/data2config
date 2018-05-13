#!/bin/python
# coding=utf-8


def getValueWrap(value, type: str):
    type = type.lower()
    # 返回属性值的包装
    if 'string' == type:
        # 转义 " 到 \"
        return '"%s"' % (value.replace('"', r'\"'))
    elif 'lstring' == type:
        return '[[%s]]' % value
    elif 'int' == type:
        return int(value) if len(value) > 0 else 0
    elif 'float' == type or 'number' == type:
        return str(float(value)) + 'f' if len(value) > 0 else '0f'
    elif 'json' == type:
        return value if len(value) > 0 else 'nil'
    elif 'bool' == type:
        return 'true' if value == 'true' or value == '1' else 'false'
    # print(value)


class TemplateInfo:
    def __init__(self, name: str, dont_rewrite: bool = False):
        self.name = name
        self.dont_rewrite = dont_rewrite


# string      name             // 文件名 xxx.csv
# string      trimmedName      // 文件名 xxx
# string      fileName         // 文件名 d:/xxx.csv
# <RowData>   data             // 数据
class CSVVo:
    def __init__(self, fileName: str, rows: ['RowData']):
        # self.data = data
        self.setFileName(fileName)
        self.rows: [RowData] = rows

    def setFileName(self, fileName: str):
        self.fileName = fileName
        idx = max(fileName.rfind('/'), fileName.rfind('\\'))
        self.name = fileName if -1 == idx else fileName[idx + 1:]
        idx = self.name.rfind('.')
        self.trimmedName = self.name if -1 == idx else self.name[:idx]


class ManageVo:
    def __init__(self):
        self.templates: [str] = None  # <str> 模板信息
        self.clsTemplates: [TemplateInfo] = []  # <str> 类的默认模板
        self.classes: [ClassVo] = []  # <Class>


# string      name            // 属性名
# string      value           // 属性值
# string      type            // 属性类型
class VarVo:
    __slots__ = ('type', 'name', 'value', 'defaultValue', 'isDel', 'isPercent',
                 'isRepeat')

    def __init__(self):
        self.type: str = None  # string 属性类型
        self.name: str = None  # string 属性名
        self.value: str = None  # string 属性值
        self.defaultValue: str = None  # string 默认值
        self.isDel: bool = False  # bool   是否已删除
        self.isPercent: bool = False  # bool   是否百分比
        self.isRepeat: bool = False

    def clone(self):
        var = VarVo()
        var.type = self.type
        var.name = self.name
        var.value = self.value
        var.defaultValue = self.defaultValue
        var.isDel = self.isDel
        var.isPercent = self.isPercent
        return var

    def valuew(self) -> str:
        return getValueWrap(self.value, self.type)

    def typew(self) -> str:
        if self.type == 'NUMBER':
            return 'float'
        return self.type


# 表示csv里的一行数据
# 模板变量 rows<RowData> 数组
# 模板变量 rowmap<rowKey, RowData>
class RowData:
    def __init__(self, cls):
        self._class: ClassVo = cls  # ClassVo 对应的类
        self.indexNames: [str] = cls.indexNames  #索引属性名列表   (仅当是map形式的时候)
        self.indexVars: [VarVo] = []  # <Var> 索引属性变量列表   (仅当是map形式的时候)
        self.originVars: [VarVo] = []  # 原始的属性列表 等同于 class.vars var.type 有效
        self.vars: [VarVo] = []  # 过滤掉删除的属性列表，类似于originVars

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
        self.csv = None  # CSVVo  csv
        self.csvName: str = None  # string csv名字
        self.templates: [str] = []  # <str> 模板名
        self.name: str = None  # string 类名
        self.isMap: bool = False  # bool   该类是否为key/value形式
        self.indexNames: [str] = []  # <string> 索引属性名列表
        self.indexs: [int] = []  # <int> 引属性值列表(不包含被删除的)
        self.vars: [VarVo] = []  # <VarVo> 变量列表(不包含被删除的)
        self.originIndexs: [int] = []  # <int> 原始的引属性值列表(包含被删除的)
        self.originVars: [VarVo] = []  # <VarVo> 原始变量列表

    def clsName(self):
        _name:str = self.name or ''
        return _name[0].upper() + _name[1:]
