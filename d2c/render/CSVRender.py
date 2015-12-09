#!/usr/bin/python
# encoding: utf-8

import csv
import os.path
from d2c.varVo import *

def getReader(filename):
    f = open(filename, 'rb')
    return csv.reader(f)
    # with open(filename, 'rb') as f:
    #     reader = csv.reader(f)
    #     return reader
        # print type(reader)
        # try:
        #     n = 0
        #     for row in reader:
        #         print reader.line_num
        #         n = n +1
        #         if n < 3:
        #             print row
        # except csv.Error as e:
        #     sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

class CSVRender:
    def __init__(self, cls, defaultTemplates, d2c):
        """
        """
        self.cls = cls
        self.defaultTemplates = defaultTemplates
        self.d2c = d2c
        self.templates = cls.templates or defaultTemplates

        self.csvName = os.path.join(d2c._config.dataDir, cls.csvName)

    def exists(self):
        return os.path.isfile(self.csvName)

    def render(self):
        rows = []
        reader = getReader(self.csvName)
        for rawRow in reader:
            # rawRow 原始的行数据
            if reader.line_num < 10:
                continue
            row = RowData(self.cls)
            rows.append(row)
            varCount = len(self.cls.vars)
            for i in range(varCount):
                var = self.cls.vars[i].clone()
                var.value = rawRow[i]
                row.vars.append(var)
            row.indexValues = [row.vars[i].value for i in self.cls.indexs]
            # print self.cls.indexs,  row.indexValues


        return rows

