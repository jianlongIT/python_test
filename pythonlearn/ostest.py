# -*- coding: utf-8 -*-
# Auther : jianlong
import os


def getall(path):
    curr = os.listdir(path)
    for x in curr:
        xpath = os.path.join(path, x)
        try:
            if os.path.isdir(xpath):
                getall(xpath)
            if os.path.isfile(xpath):
                print(xpath)
        except PermissionError as e:
            continue


getall('/Users/dongzhiqiao')
