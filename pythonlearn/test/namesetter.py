# -*- coding: utf-8 -*-
# Auther : jianlong
class Nametest(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


jianlong = Nametest('jianlong')
print(jianlong.name)
jianlong.name = 'guojianlong'
print(jianlong.name)
