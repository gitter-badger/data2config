#!/usr/bin/python
# encoding: utf-8

import csv
import os.path
from d2c.varVo import *

import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect="excel", encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

def getReader(filename):
    f = open(filename, 'rb')
    return UnicodeReader(f, encoding='gbk')
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
        line_num = 1
        for rawRow in reader:
            # rawRow 原始的行数据
            if line_num < 10:
                line_num += 1
                continue
            row = RowData(self.cls)
            rows.append(row)
            originCount = len(self.cls.originVars)
            for i in xrange(originCount):
                var = self.cls.originVars[i].clone()
                var.value = rawRow[i]
                row.originVars.append(var)
                if not var.isDel:
                    row.vars.append(var)
            row.indexVars = [row.vars[i] for i in self.cls.indexs]
            # print self.cls.indexs,  row.indexValues


        return rows

