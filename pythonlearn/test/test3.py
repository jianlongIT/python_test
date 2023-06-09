# -*- coding: utf-8 -*-
# Auther : jianlong
import time


def out(func):
    def inner(*args, **kwargs):
        print('args', args, 'kwargs', kwargs)
        if args == 'jianlong':
            print('jianlong')
        result = func(*args, **kwargs)
        return result

    return inner


@out
def test(name):
    return name


s = {'name': 'jianlong'}
name1 = test(name=s)
print(name1)


def timetest(fund):
    def inner(*args, **kwargs):
        start = time.time()
        print('程序开始运行')
        result = fund(*args, **kwargs)
        print('程序结束运行')
        end = time.time()
        print('函数{}的运行时间为{}'.format(fund.__name__, end - start))
        return result

    return inner


@timetest
def test2(name2):
    time.sleep(1)
    return name2


name3 = test2('鉴龙')
print(name3)
