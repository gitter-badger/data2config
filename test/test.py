#!/bin/python
# coding=utf-8

import sys
import os, os.path
path = os.path.normpath(os.path.join(__file__, '../..'))
sys.path.append(path)


from jinja2 import Template
from jinja2 import Environment, PackageLoader
from d2c.parsers.defParser import DefParser
import csv
import os, os.path
import sys

def doxxx():
    env = Environment(loader=PackageLoader('d2c', 'templates'))
    

    # simplate data
    data = dict()
    data['smartUpdateKey'] = 'this is smartUpdateKey'
    data['allSprites'] = [
        {'trimmedName':'_trimmedName', 'frameRect':{'x':100, 'y':200, 'width':20, 'height':30}},
        {'trimmedName':'_trimmedName', 'frameRect':{'x':100, 'y':200, 'width':20, 'height':30}}
    ]

    template = env.get_template('template.txt')
    print template.render(**data)

    # class data
    allClasses = []
    allClasses.append({'name':'Class1', 'varlist':[{'name':'v1', 'value':1},{'name':'v2', 'value':2}],'indexkeys':['name']})
    allClasses.append({'name':'Class2', 'varlist':[{'name':'v1', 'value':1},{'name':'v2', 'value':2}],'indexkeys':['name']})
    template = env.get_template('StaticData.txt')
    # print template.render(allClasses = allClasses)

    classData = []
    classData.append({'varlist':[{'name':'v1', 'value':1},{'name':'v2', 'value':2}],'indexvalues':['v1', 2]})
    classData.append({'varlist':[{'name':'v1', 'value':3},{'name':'v2', 'value':4}],'indexvalues':['v3', 4]})
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


def testTemplate():
    env = Environment(loader=PackageLoader('test', 'templates'))

    data = readfile('staticvo.txt')
    parser = DefParser()
    parser.parse(data)

    manage = parser.manage
    template = env.get_template(manage.templateNames[0])

    writefile('xxx.txt', template.render(allClasses=manage.classes))


    
def testCsv():
    filename = 'csv/effect.csv'
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        print type(reader)
        try:
            n = 0
            for row in reader:
                print reader.line_num
                n = n +1
                if n < 3:
                    print row
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


if __name__ == "__main__":
    # testCsv()
    testTemplate()
