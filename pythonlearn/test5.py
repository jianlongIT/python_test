# -*- coding: utf-8 -*-
# Auther : jianlong
from datetime import datetime, timedelta
import datetime as datetime2

now1 = datetime2.datetime.now()
now2 = datetime.now()
print(now1, now2)

print(now1.date(), now2.time())

date_str1 = now1.date().strftime('%Y-%m-%d')
print(date_str1)
time_str2 = now2.time().strftime('%H:%M:%S')
print(time_str2)

date_time3 = date_str1 + ' ' + time_str2
print(date_time3)
print(datetime2.datetime.strptime(date_time3, '%Y-%m-%d %H:%M:%S'))

str1 = '2019-09-10 8:10:56'
print(datetime.strptime(str1, '%Y-%m-%d %H:%M:%S'))

print(datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S'))
now3 = datetime.now()
timedelta1 = timedelta(days=3, hours=6, minutes=12)
before = now3 - timedelta1
print(before)
