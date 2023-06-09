# -*- coding: utf-8 -*-
# Auther : jianlong

t_1 = (x for x in range(10))  # 结果是生成器对象，使用tuple()函数将其转换为元组
tuple1 = tuple(t_1)
for i in tuple1:
    print(i)
    break
else:
    print('结束')

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)

nums = (
    1121, 3, 43, 43, 53252351111, 666666234234, 5234234, 4234, 4234, 423423, 4234, 423, 42, 4234234234, 4234234, 42342,
    42342344)
max = 0
for i in nums:
    if i > max:
        max = i
    else:
        continue
else:
    print(max)

# for i in range(1, 10):
#    for j in range(1, 10):
#        if j <= i:
#            print('{} * {} = {}   '.format(j, i, i * j), end='')
#    print('\n\r')

i = 1
j = 1
while i < 10:
    while j < 10:
        if j <= i:
            print('{} * {} = {}   '.format(j, i, i * j), end='')
        j += 1
    else:
        j = 1
    i += 1
    print('\n\r')

num2 = 0
for i in range(100):
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        num2 += 1
print(num2)

dict1 = ['{} * {} = {}'.format(i, j, i * j, end='') for i in range(1, 10) for j in range(1, 10) if i <= j]
print(dict1)
