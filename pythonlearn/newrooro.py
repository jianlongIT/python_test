# -*- coding: utf-8 -*-
# Auther : jianlong
class Newerror(Exception):
    def __init__(self, message):
        self.message = message
