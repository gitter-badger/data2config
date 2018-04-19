#!/usr/bin/python
# coding=utf-8

from litefeel.pycommon.io import read_file
import yaml
import os


def make_arr(s) -> [str]:
    if s is None:
        return []
    if isinstance(s, str):
        return [str]
    return s


class Config:
    def __init__(self):
        self.idlPath = None  # 描述文档路径
        self.templateDir = ''  # 模板文件目录
        self.outputDir = None  # 输出文件目录
        self.dataDir = None  # 输入文件目录
        self.main_templates: [str] = []
        self.cls_templates: [str] = []

    def load(self, path) -> 'Config':
        data = read_file(path)
        data = yaml.load(data)
        root = os.path.dirname(path)
        self.templateDir = os.path.join(root, data['template_dir'])
        self.outputDir = os.path.join(root, data['output_dir'])
        self.dataDir = os.path.join(root, data['data_dir'])
        self.main_templates = make_arr(data['main_templates'])
        self.cls_templates = make_arr(data['cls_templates'])
        return self

    def setIdlPath(self, path):
        self.idlPath = path

    def setTemplateDir(self, path):
        self.templateDir = path

    def setOutputDir(self, path):
        self.outputDir = path

    def setDataDir(self, path):
        self.dataDir = path
