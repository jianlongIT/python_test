# -*- coding: utf-8 -*-
# Auther : jianlong
class persion(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('我是 %s' % self.name)


class student(persion,object):
    def __init__(self, score, major, __stu_num, name, gender):
        self.score = score
        self.major = major
        self.__stu_num = __stu_num
        super().__init__(name, gender)

    def speak(self):
        super(student, self).speak()
        print('我的学号为 %s 很高兴认识大家' % self.__stu_num)

    def identify_stu(self):
        if self.__stu_num == '2018014002':
            print('我的分组已经完成')

    def rel(self):
        if isinstance(self, persion) and issubclass(student, persion):
            print('我的父类是', self.__class__.__base__.__name__)


stu1 = student('99', '11', '2018014002', 'jianlong', 'boy')
stu1.speak()
stu1.identify_stu()
stu1.rel()
