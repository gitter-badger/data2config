#!/bin/python
# coding=utf-8

import os
import sys

from jinja2 import Environment, FileSystemLoader, Template
from litefeel.pycommon.io import read_file, write_file

from .config import Config
from .function import indexOfKey, output_filter
from .parsers.excelHead import ExcelParser
from .render.ExcelRender import ExcelRender
from .varVo import ManageVo


class D2C:
    def __init__(self, config: Config):
        self._config = config

        self._idlParser = None

        self._env = None

    def doD2c(self):
        self._env = Environment(
            loader=FileSystemLoader(self._config.templateDir))

        manage = ManageVo()
        manage.clsTemplates = self._config.cls_templates
        manage.templates = self._config.main_templates

        for root, _, files in os.walk(self._config.dataDir):
            for f in files:
                # ~$ 开头为excel打开后的临时文件
                if f.endswith('xlsx') and not f.startswith('~$'):
                    clsVo = ExcelParser.parse(os.path.join(root, f))
                    manage.classes.append(clsVo)

        for template_name in manage.templates:
            template = self._env.get_template(template_name)
            outputData = template.render(classes=manage.classes)
            outputData, outputName = output_filter(outputData)
            if (outputName is None):
                outputName = template_name

            outputName = os.path.join(self._config.outputDir, outputName)

            write_file(outputName, outputData)

        for cls in manage.classes:
            render = ExcelRender(cls, manage.clsTemplates, self)
            if not render.exists():
                continue
            print("正在处理数值表: %s" % cls.csvName)
            rows = render.render()
            for template_name in render.templates:
                template = self._env.get_template(template_name)
                args = {'rows': rows, 'class': cls}
                # print(cls.csvName)
                outputData = template.render(**args)
                outputData, outputName = output_filter(outputData)
                if (outputName is None):
                    outputName = template_name

                outputName = os.path.join(self._config.outputDir, outputName)

                write_file(outputName, outputData)
