# -*- coding: utf-8 -*-
# Auther : jianlong

class test(object):
    def __str__(self):
        return '对象信息'

    def search(self, *args, **kwargs):
        print(args)
        print(kwargs)


    def __init__(self, attr=''):
        self.__attr = attr

    def __getattr__(self, item):
        if self.__attr:
            key = '{},{}'.format(self.__attr, item)
            print('属性存在', id(self), key)
        else:
            key = item
            print('属性不存在', id(self), key)
        ts = test(key)
        return ts

    def __call__(self, *args, **kwargs):
        print("call1 ", self.__attr, "     ---call2-构造  前- ", id(self), *args, '\n\n')


t = test()
kws = {
    'name': 'jianlong',
    'age': 26
}
a = 1
t.search(a, **kws)
