# coding:utf-8

import sys


a=[1,2]
b=[3,4]
print(id(a))
a.append(3)
a=a+b
print(a,id(a))
c=(1,2,[1,2])
d=(3,4)
print(id(c))
c[2].append(4)
print(c,id(c))