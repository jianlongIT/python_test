# -*- coding: utf-8 -*-
# Auther : jianlong
from datetime import datetime, timedelta


def cat():
    print('get cat')


def second_cat():
    print('second cat')


time1 = datetime.now()
time12 = datetime(2023, 6, 5, 12, 12, 24, 223)
yesterday = timedelta(days=1)
time13 = time12 - yesterday
print(time1)
print(time12)
str_time = time13.strftime('%Y-%m-%d %H:%M:%S %f')
print(str_time, type(str_time))
print(datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S %f'))
