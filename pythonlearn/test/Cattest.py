# -*- coding: utf-8 -*-
# Auther : jianlong

class Cat(object):

    def __init__(self, color, age, name):
        self.color = color
        self.age = age
        self.name = name

    def show(self):
        print('我是 %s，我今年 %d 岁，我是%s色的' % (self.name, self.age, self.color))


charllote = Cat('红', 2, 'charllote')
charllote.show()
