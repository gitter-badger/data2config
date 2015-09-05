#!/bin/python
# coding=utf-8



# string      name             // 文件名 xxx.csv
# string      trimmedName      // 文件名 xxx
# string      fileName         // 文件名 d:/xxx.csv
# <<value>>   data             // 数据 [line][column]
class CSVVo:
    def __init__(self, fileName, data):
        self.data = data
        self.setFileName(fileName)

    def setFileName(fileName):
        self.fileName = fileName
        idx = max(fileName.rfind('/'), fileName.rfind('\\'))
        self.name = fileName if -1 == idx else fileName[idx+1:]
        idx = self.name.rfind('.')
        self.trimmedName = self.name if -1 == idx else self.name[:idx]



# <string> templateNames         // 管理类的模板名
# <string> clsTemplateNames      // 类的默认模板名
class ManageVo:
    def __init__(self):
        self.templateNames = None
        self.clsTemplateNames = None
        self.classes = []
        self._templates = None       # Template 模板
        self._clsTemplates = None    # Template 类模板

# string      name            // 属性名
# string      value           // 属性值
# string      type            // 属性类型
class VarVo:
    def __init__(self):
        self.type = None                       # string 属性类型
        self.name = None                       # string 属性名
        self.value = None                      # string 属性值
        self.isDel = False                     # bool   是否已删除
        self.isPercent = False                 # bool   是否百分比


# CSV         csv              // 对应的csv
# <string>    templateNames    // 对应的模板名
# string      name             // 类名
# <string>    indexNames       // 索引属性名列表
# <str|num>   indexValues      // 索引属性值列表
# bool        isMap            // 是否索引为key
# <Var>       vars             // 属性列表
class ClassVo:
    def __init__(self):
        self.csv = None                         # CSVVo  csv
        self.svnName = None                     # string csv名字
        self.templateNames = None               # <string> 模板名
        self.name = None                        # string 类名
        self.isMap = True                       # bool   该类是否为key/value形式
        self.indexNames = []                    # <string> 索引属性名列表
        self.indexValues = []                   # <str|num> 索引属性值列表
        self.indexVars = []                     # <VarVo> 索引变量列表
        self.vars = []                          # <VarVo> 变量列表
        self._templates = None                  # <Template> 模板

    def setIndexNames(names):
        # <string> names 索引的参数列表

        if names is None or len(names) == 0:
            isMap = False
            return

        for name in names:
            v = self._getVarIdx(name)
            if v is not None:
                self.indexNames.append(name)
                self.indexValues.append(v.value)
                self.indexVars.append(v)
            else:
                raise NameError('can not parse getItem for key: %s' % (name))


    def _getVar(varName):
        for v in self.vars:
            if v.name == varName:
                return v
        return None
