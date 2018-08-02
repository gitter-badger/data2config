#!/usr/bin/python
# encoding=utf-8

class A:
    y = 5
    def __init__(self):
        self.x = 0

    def __getitem__(self, key):
        # call by obj[key]
        print '__getitem__', key
        return 1

    def __getattr__(self, key):
        # call by obj.key
        print '__getattr__', key
        return 2

    def aaa(self):
        print 'aaa'

    def __aaa(self):
        # 多个_开始并不以_结尾的方法会自动添加_$className前缀
        # _A__aaa
        print '__aaa'

    def __aaa(self):
        # _A___aaa
        print '__aaa'

    def __aaa__(self):
        print '__aaa__'

    def _aaa(self):
        print '_aaa'





a = A()
a.k
a['k']
a._A__aaa()
print "a.__dict__"
print a.__dict__
print "A.__dict__"
print A.__dict__



# obj.__dict__ 只有属性，不包括方法
# Cls.__dict__ 包括属性和方法
