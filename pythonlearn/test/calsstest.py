# -*- coding: utf-8 -*-
# Auther : jianlong

class Cat(object):
    def __init__(self, name):
        self.__name = name

    def __run(self):
        print("{} is run".format(self.__name))

    def torun(self):
        self.__run()


cat = Cat('charllote')

cat.torun()
