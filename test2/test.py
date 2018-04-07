#!/bin/python
# coding=utf-8

import sys
import os, os.path
abspath = os.path.abspath(os.path.join(__file__, '../..'))

sys.path.append(abspath)

# reload(sys)
# sys.setdefaultencoding('utf-8')

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from d2c.parsers.defParser import DefParser
from d2c.d2c import D2C
from d2c.config import Config
import csv
import os, os.path
import sys

testpath = os.path.dirname(os.path.abspath(__file__))
templatespath = os.path.join(testpath, 'myapp/templates/json')
myapppath = os.path.join(testpath, 'myapp')


def doxxx():
    env = Environment(loader=FileSystemLoader('d2c', templatespath))

    # simplate data
    data = dict()
    data['smartUpdateKey'] = 'this is smartUpdateKey'
    data['allSprites'] = [{
        'trimmedName': '_trimmedName',
        'frameRect': {
            'x': 100,
            'y': 200,
            'width': 20,
            'height': 30
        }
    }, {
        'trimmedName': '_trimmedName',
        'frameRect': {
            'x': 100,
            'y': 200,
            'width': 20,
            'height': 30
        }
    }]

    template = env.get_template('template.txt')
    print(template.render(**data))

    # class data
    allClasses = []
    allClasses.append({
        'name':
        'Class1',
        'varlist': [{
            'name': 'v1',
            'value': 1
        }, {
            'name': 'v2',
            'value': 2
        }],
        'indexkeys': ['name']
    })
    allClasses.append({
        'name':
        'Class2',
        'varlist': [{
            'name': 'v1',
            'value': 1
        }, {
            'name': 'v2',
            'value': 2
        }],
        'indexkeys': ['name']
    })
    template = env.get_template('StaticData.txt')
    # print template.render(allClasses = allClasses)

    classData = []
    classData.append({
        'varlist': [{
            'name': 'v1',
            'value': 1
        }, {
            'name': 'v2',
            'value': 2
        }],
        'indexvalues': ['v1', 2]
    })
    classData.append({
        'varlist': [{
            'name': 'v1',
            'value': 3
        }, {
            'name': 'v2',
            'value': 4
        }],
        'indexvalues': ['v3', 4]
    })
    template = env.get_template('class.txt')
    # print template.render(allClassData=classData)

    # template = Template('Hello {{ name }}')
    # data = template.render(name='John Doe')
    # print data


def readfile(filename):
    if not os.path.exists(filename):
        return None
    with open(filename) as f:
        data = f.read()
        f.close()
        return data


def writefile(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
        f.close()


# self.idlPath = None                # 描述文档路径
#         self.templateDir = ''              # 模板文件目录
#         self.outputDir = None              # 输出文件目录
#         self.dataDir = None
def testTemplate():

    config = Config()
    config.idlPath = os.path.join(myapppath, 'staticvo.txt')
    config.templateDir = os.path.join(myapppath, 'templates/lua')
    config.outputDir = os.path.join(myapppath, '../dest')
    config.dataDir = os.path.join(myapppath, 'excel')
    d2c: D2C = D2C(config)
    d2c.doD2c()

    # env = Environment(loader=FileSystemLoader(templatespath))
    # print templatespath
    # data = readfile(os.path.join(testpath, 'myapp/staticvo.txt'))
    # parser = DefParser()
    # parser.parse(data)

    # # parser.setDataParse()

    # manage = parser.manage
    # template = env.get_template(manage.templateNames[0])

    # writefile(os.path.join(testpath, 'dest/StaticData.lua'), template.render(allClasses=manage.classes))


def testCsv():
    filename = os.path.join(testpath, 'myapp/csv/effect.csv')
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        print(type(reader))
        try:
            n = 0
            for row in reader:
                print(reader.line_num)
                n = n + 1
                if n < 3:
                    print(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


if __name__ == "__main__":
    # testCsv()
    testTemplate()
