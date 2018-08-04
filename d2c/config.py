#!/usr/bin/python
# coding=utf-8

from __future__ import annotations

import os
from typing import Dict, List

import yaml
from litefeel.pycommon.io import read_file

from .function import dict_key, dict_value
from .varVo import TemplateInfo


def make_data_filter(s: str) -> str:
    if not s:
        return None
    assert isinstance(s, str), 'data_filter in config must be string'
    return s.strip().upper()


# return (k, v)
def first(dic):
    for k, v in dic.items():
        return (k, v)
    return (None, None)


def make_infos(s: [any]) -> [TemplateInfo]:
    if s is None:
        return []
    assert isinstance(s, list), 'config template type error'
    arr = []
    for v in s:
        if isinstance(v, str):
            arr.append(TemplateInfo(v))
        elif isinstance(v, dict):
            assert len(v) == 1, 'config template dict error'
            arr.append(TemplateInfo(*first(v)))
        else:
            raise NameError('config template type error')
    return arr


def make_info_dict(arr: [any]) -> Dict[str, [TemplateInfo]]:
    if not arr:
        return {}

    assert isinstance(arr, list), 'specific_template must is a list'

    tmp_dict: Dict[str, [TemplateInfo]] = {}

    for excel_entry in arr:
        assert isinstance(excel_entry,
                          dict), 'any item must be map in specific_template'
        assert len(excel_entry) == 1, 'specific_template parse error'
        key = dict_key(excel_entry)
        assert isinstance(key, str)
        assert key not in tmp_dict, 'has dumplecation data fiel in specific_template'
        temps = make_infos(dict_value(excel_entry))
        assert len(
            temps
        ) > 0, 'data file: %s in specific_template must have template' % key
        tmp_dict[key] = temps

    return tmp_dict


class Config:
    def __init__(self):
        self.templateDir: str = ''  # 模板文件目录
        self.outputDir: str = None  # 输出文件目录
        self.dataDir: str = None  # 输入文件目录
        self.data_filter: str = None  # 数据过滤器，当不为空时，只有包含该过滤器内容的字段才会被输出
        self.main_templates: [TemplateInfo] = []
        self.cls_templates: [TemplateInfo] = []
        self.specific_template: Dict[str, [TemplateInfo]] = {}

    def load(self, path) -> Config:
        data = read_file(path)
        data: Dict[str, any] = yaml.load(data)
        root = os.path.dirname(path)
        self.data_filter = make_data_filter(data.get('data_filter'))
        self.templateDir = os.path.join(root, data['template_dir'])
        self.outputDir = os.path.join(root, data['output_dir'])
        self.dataDir = os.path.join(root, data['data_dir'])
        self.main_templates = make_infos(data['main_templates'])
        self.cls_templates = make_infos(data['cls_templates'])
        self.specific_template = make_info_dict(data['specific_template'])
        return self

    # def setTemplateDir(self, path):
    #     self.templateDir = path

    # def setOutputDir(self, path):
    #     self.outputDir = path

    # def setDataDir(self, path):
    #     self.dataDir = path

    def get_templates(self, filename: str) -> [TemplateInfo]:
        arr = self.specific_template.get(filename)
        if not arr:
            arr = self.cls_templates
        return arr
