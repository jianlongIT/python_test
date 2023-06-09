# -*- coding: utf-8 -*-
# Auther : jianlong

import os


def second_test():
    print('second test')


s = 1
a = 2
m = []
print('名称' + __name__)
is_main = __name__ == '__main__'
print(is_main)
if is_main:
    print(__name__)
    a = input("请输入一个数字")
    print('输入的数字' + a)
    name = input("你的名字是：")
    print("你输入的名字是: %s" % (name
                           ))
    money = input('你好，请输入付款金额：')
    print('付款成功，您本次支付' + money + '元。')
