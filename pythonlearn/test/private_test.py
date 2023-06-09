# -*- coding: utf-8 -*-
# Auther : jianlong
class Cat(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __jump(self):
        print('%d的 %s 在jump ' % (self.__age, self.name))

    def jump(self):
        self.__jump()

    def run(self):
        self.__jump()


tom = Cat('tom', 33)
tom.jump()
