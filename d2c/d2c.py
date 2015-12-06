#!/bin/python
# coding=utf-8

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from parsers.defParser import DefParser
from function import *
import csv
import os, os.path
import sys




class D2C:
    def __init__(self, config):
        self._config = config

        self._idlParser = None

        self._env = None


    def doD2c(self):
        self._env = Environment(loader=FileSystemLoader(self._config.templateDir))
        data = readfile(self._config.idlPath)


        parser = DefParser()
        parser.parse(data)

        manage = parser.manage
        template = self._env.get_template(manage.templateNames[0])
        print(template)

        outputData = template.render(classes=manage.classes)
        outputData, outputName = output_filter(outputData)
        if (outputName is None):
            outputName = template.name

        outputName = os.path.join(self._config.outputDir, outputName)

        writefile(outputName, outputData)
        
