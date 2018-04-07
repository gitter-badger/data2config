#!/bin/python
# coding=utf-8

import csv
import os
import os.path
import sys

abspath = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(abspath)

from jinja2 import Environment, FileSystemLoader, Template

from d2c.config import Config
from d2c.d2c import D2C
from d2c.parsers.defParser import DefParser





# reload(sys)
# sys.setdefaultencoding('utf-8')


testpath = os.path.dirname(os.path.abspath(__file__))
templatespath = os.path.join(testpath, 'myapp/templates/json')
myapppath = os.path.join(testpath, 'myapp')


def testTemplate(configpath: str):
    config = Config().load(configpath)
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
    configpath = os.path.join(myapppath, 'config.yml')
    # print(sys.argv)
    if len(sys.argv) == 2:
        configpath = sys.argv[1]
    testTemplate(configpath)

