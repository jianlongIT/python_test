# -*- coding: utf-8 -*-
# Auther : jianlong
num1 = 1
num2 = 2
s = 0


def getsum():
    global num2
    global num1
    global s
    num = num2
    num2 += num1
    num1 = num
    s += 1
    if s < 27:
        getsum()
    else:
        print(num1 + num2)


getsum()
