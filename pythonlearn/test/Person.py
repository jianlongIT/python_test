# -*- coding: utf-8 -*-
# Auther : jianlong

class Person():
    name = "G jianlong"

    def hup(self):
        print("{} is hup".format(self.name))
        print("%s is hup" % self.name)


jianlong = Person()
jianlong.name = 'ss'
jianlong.hup()


def test(a):
    print(a.name)


test(jianlong)
