#!/usr/bin/python
# coding=utf-8

from litefeel.pycommon.io import read_file
import yaml
import os
from .varVo import TemplateInfo


def make_arr(s) -> [str]:
    if s is None:
        return []
    if isinstance(s, str):
        return [str]
    return s

# return (k, v)
def first(dic):
    for k, v in dic.items():
        return (k, v)
    return (None, None)

def make_infos(s) -> [TemplateInfo]:
    if s is None:
        return []
    if not isinstance(s, (list, tuple)):
        raise NameError('config template type error')
    arr = []
    for v in s:
        if isinstance(v, str):
            arr.append(TemplateInfo(v))
        elif isinstance(v, dict):
            if len(v) != 1:
                raise NameError('config template dict error')
            arr.append(TemplateInfo(*first(v)))
        else:
            raise NameError('config template type error')
    return arr


class Config:
    def __init__(self):
        self.idlPath = None  # 描述文档路径
        self.templateDir = ''  # 模板文件目录
        self.outputDir = None  # 输出文件目录
        self.dataDir = None  # 输入文件目录
        self.main_templates: [TemplateInfo] = []
        self.cls_templates: [TemplateInfo] = []

    def load(self, path) -> 'Config':
        data = read_file(path)
        data = yaml.load(data)
        root = os.path.dirname(path)
        self.templateDir = os.path.join(root, data['template_dir'])
        self.outputDir = os.path.join(root, data['output_dir'])
        self.dataDir = os.path.join(root, data['data_dir'])
        self.main_templates = make_infos(data['main_templates'])
        self.cls_templates = make_infos(data['cls_templates'])
        return self

    def setIdlPath(self, path):
        self.idlPath = path

    def setTemplateDir(self, path):
        self.templateDir = path

    def setOutputDir(self, path):
        self.outputDir = path

    def setDataDir(self, path):
        self.dataDir = path
