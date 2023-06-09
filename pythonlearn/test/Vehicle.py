# -*- coding: utf-8 -*-
# Auther : jianlong

class Vehicle(object):
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def inf(self):
        print(type(self.size))
        print('这是一辆{}  体积是{}'.format(self.type, self.size))


car = Vehicle('suv', (10, 10, 10))
car.inf()
