# -*- coding: utf-8 -*-
# Auther : jianlong

# coding:utf-8

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        print('该图形的初始点为:{X: %s, Y: %s}' % (self.x, self.y), end='')


class Circle(Point):
    def __init__(self, radius, x, y):
        self.radius = radius
        super(Circle, self).__init__(x, y)

    def string(self):
        print('该图形初始点为:{X: %s, Y: %s};{半径为: %s}' % (self.x, self.y, self.radius))


class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def string(self):
        print('长宽分别为:{Width: %s, Height: %s}' % (self.width, self.height))


class Rectangle(Point, Size,Test):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    def string(self):
        Point.string(self)
        Size.string(self)
        Test.string(self)


if __name__ == '__main__':
    c = Circle(radius=8, x=5, y=5)
    c.string()
    r = Rectangle(x=15, y=15, width=15, height=15)
    r.string()
    r_1 = Rectangle(x=40, y=30, width=11, height=14)
    r_1.string()
