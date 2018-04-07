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


def testTemplate():
    config = Config().load(os.path.join(myapppath, 'config.yml'))
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


if __name__ == "__main__":
    # testCsv()
    testTemplate()
