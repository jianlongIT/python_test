# -*- coding: utf-8 -*-
# Auther : jianlong
import os

current_path = os.getcwd()
print(current_path)
if not os.path.exists('py'):
    os.mkdir('py')
print(os.path.isabs('/Users/dongzhiqiao/test'))
print(os.path.abspath('test1'))


print(os.path.isdir(current_path))


