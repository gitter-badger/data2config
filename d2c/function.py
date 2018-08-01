#!/usr/bin/python
# coding=utf-8

import os.path
import re

# filename:xxxxx.xxx
# ---------
# 这种格式表示文件信息，不会输出到文件
P_OUTPUT_FILTER = 'filename:(.+)\r?\n---+\r?\n(.+)'  # filename:xxxxx\n---\n.*


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


def upper_first(s: str) -> str:
    if len(s) > 0:
        return s[0].upper() + s[1:]
    return s