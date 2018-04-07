#!/usr/bin/python
# coding=utf-8


class Config:
    def __init__(self):
        self.idlPath = None  # 描述文档路径
        self.templateDir = ''  # 模板文件目录
        self.outputDir = None  # 输出文件目录
        self.dataDir = None  # 输入文件目录

    def setIdlPath(self, path):
        self.idlPath = path

    def setTemplateDir(self, path):
        self.templateDir = path

    def setOutputDir(self, path):
        self.outputDir = path

    def setDataDir(self, path):
        self.dataDir = path
