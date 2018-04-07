#!/bin/python
# coding=utf-8

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from .parsers.defParser import DefParser
from .render.ExcelRender import ExcelRender
from .config import Config
from litefeel.pycommon.io import read_file, write_file
from .function import indexOfKey, output_filter
import csv
import os, os.path
import sys


class D2C:
    def __init__(self, config: Config):
        self._config = config

        self._idlParser = None

        self._env = None

    def doD2c(self):
        self._env = Environment(
            loader=FileSystemLoader(self._config.templateDir))
        data = read_file(self._config.idlPath)

        parser = DefParser()
        parser.parse(data)

        manage = parser.manage

        for info in manage.templates:
            template = self._env.get_template(info.name)
            outputData = template.render(classes=manage.classes)
            outputData, outputName = output_filter(outputData)
            outputName = info.outputName or outputName
            if (outputName is None):
                outputName = template.name

            outputName = os.path.join(self._config.outputDir, outputName)

            write_file(outputName, outputData)

        for cls in manage.classes:
            render = ExcelRender(cls, manage.clsTemplates, self)
            if not render.exists():
                continue
            rows = render.render()
            for info in render.templates:
                template = self._env.get_template(info.name)
                args = {'rows': rows, 'class': cls}
                print(cls.csvName)
                outputData = template.render(**args)
                outputData, outputName = output_filter(outputData)
                outputName = info.outputName or outputName
                if (outputName is None):
                    outputName = template.name

                outputName = os.path.join(self._config.outputDir, outputName)

                write_file(outputName, outputData)
