# -*- coding: utf-8 -*-
# Auther : jianlong
import sys
import os

modules = sys.modules
for k, v in modules.items():
    # print(k, '---------', v)
    pass

print(sys.getdefaultencoding())
print(sys.platform)
print(sys.version)
print(sys.path)
print(sys.argv)
print(os.getcwd())
open('/Users/dongzhiqiao/PycharmProjects/pythonlearn/test.txt', 'w').write('hello jianlong')
