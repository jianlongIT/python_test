# -*- coding: utf-8 -*-
# Auther : jianlong
import time
from datetime import datetime

time1 = time.localtime()
print(time1.tm_year)

times = datetime.timestamp(datetime.now())
print(times, type(times))

time_obj = datetime.fromtimestamp(times)
print(time_obj, type(time_obj))
print(type(datetime.strftime(time_obj, '%Y-%m-%d %H:%M:%S')))
print(type(datetime.strptime(datetime.strftime(time_obj, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')))

time1 = datetime.now().time()
print(time1, type(time1))
date1 = datetime.now().date()
print(date1, type(date1))