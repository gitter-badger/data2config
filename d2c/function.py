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
    with open(filename, 'w') as f:
        f.write(data)
        f.close()


P_OUTPUT_FILTER    = 'filename:(.+)\r?\n\-\-\-+\r?\n(.+)'    # filename:xxxxx\n---\n.*

def output_filter(output):
    """return [output, filename], filename can None
    """
    r = re.match(P_OUTPUT_FILTER, output, re.S)
    if r is None:
        return output, None
    print output
    return r.group(2), r.group(1).strip()