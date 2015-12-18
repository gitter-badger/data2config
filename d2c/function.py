#!/usr/bin/python
# coding=utf-8

import os.path
import re

def readfile(filename):
    if not os.path.exists(filename):
        return None
    with open(filename) as f:
        data = f.read()
        f.close()
        return data

def writefile(filename, data):
    dirname = os.path.dirname(filename)
    if len(dirname) > 0 and not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, 'w') as f:
        f.write(data)
        f.close()


# filename:xxxxx.xxx
# ---------
# 这种格式表示文件信息，不会输出到文件
P_OUTPUT_FILTER    = 'filename:(.+)\r?\n\-\-\-+\r?\n(.+)'    # filename:xxxxx\n---\n.*

def output_filter(output):
    """return [output, filename], filename can None
    """
    r = re.match(P_OUTPUT_FILTER, output, re.S)
    if r is None:
        return output, None
    # print output
    return r.group(2), r.group(1).strip()


def indexOfKey(array, value, key):
    i = -1
    for v in array:
        i += 1
        if v[key] == value:
            return i
    return -1
