#!/usr/bin/python
# coding=utf-8

import os.path

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
