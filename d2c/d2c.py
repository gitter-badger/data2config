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
from .varVo import ClassVo, TemplateInfo


class D2C:
    def __init__(self, config: Config):
        self._config: Config = config
        self._env: Environment = None

    def doD2c(self):
        self._env = Environment(
            loader=FileSystemLoader(self._config.templateDir))

        classes: [ClassVo] = []
        for root, _, files in os.walk(self._config.dataDir):
            for f in files:
                # ~$ 开头为excel打开后的临时文件
                if f.endswith('xlsx') and not f.startswith('~$'):
                    clsVo = ExcelParser.parse(os.path.join(root, f), self._config)
                    classes.append(clsVo)

        self.render_managers(self._config, classes)
        self.render_classes(self._config, classes)

    def render_managers(self, config: Config, classes: [ClassVo]):
        for template_info in config.main_templates:
            template = self._env.get_template(template_info.name)
            outputData = template.render(classes=classes)
            outputData, outputName = output_filter(outputData)
            if (outputName is None):
                outputName = template_info.name

            outputName = os.path.join(self._config.outputDir, outputName)

            if not template_info.dont_rewrite or not os.path.exists(outputName):
                write_file(outputName, outputData)

    def render_classes(self, config: Config, classes: [ClassVo]):
        for cls in classes:
            templates = config.get_templates(cls.csvName)
            render = ExcelRender(cls, templates, self)
            if not render.exists():
                continue
            print("正在处理数值表: %s" % cls.csvName)
            rows = render.render()
            for template_info in render.templates:
                template = self._env.get_template(template_info.name)
                args = {'rows': rows, 'class': cls}
                # print(cls.csvName)
                outputData = template.render(**args)
                outputData, outputName = output_filter(outputData)
                if (outputName is None):
                    outputName = template_info.name

                outputName = os.path.join(self._config.outputDir, outputName)

                if not template_info.dont_rewrite or not os.path.exists(
                        outputName):
                    write_file(outputName, outputData)
