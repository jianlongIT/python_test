# -*- coding: utf-8 -*-
# Auther : jianlong
from animal.cat import cat
from animal.dog.dog import dog
import time
from test1 import test1
from test.second import second_test
from test.alist import alit


def upper(str):
    result = ''
    try:
        result = str.upper()
    except Exception as e:
        print("程序出错了")
        print(e)
    return result


result = upper(1)
print(result)

second_test()
cat()
dog()
time.time()
print(result)
result = test1.test()
print(result)
alit()
