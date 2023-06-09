# -*- coding: utf-8 -*-
# Auther : jianlong

tuple1 = (1, 2, 3)

list1 = list(tuple1)
print(list1, type(list1))
set1 = set(list1)
print(set1, type(set1))

s = "ajldjlajfdljfddd";
print(sorted(list(s)))
print(sorted(set(list(s))))

s1 = ('1', '2', '3')
print('@'.join(s1))

s = 'i am jianlong'
slist = s.split()
print(slist)
for i in slist:
    print(i)
    if i == 'jianlong' or i == 'am':
        slist[slist.index(i)] = 'sss'
print(slist)

for i in range(1, 10):
    print('i:', i)

print(10 % 2)

s = '%s is dasda  %s' % ('jianlong', 'jianlong2')
print(s)

sk = {
    "s": {
        "ad": "ad",
        "ac": "ac"
    }
}

print("ad" in sk.get("s"))

for a, b in sk.get('s').items():
    print(a, b)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

dict1 = {}
for i in range(1, 9):
    dict1[i] = i * i
print(dict1)

num1 = 0
for i in range(1, 1001):
    if i % 2 != 0:
        num1 += i
print('num1:', num1)

print({x: x ** 2 for x in range(10)})
print({x for x in range(10)})

t_1 = (x for x in range(10))  # 结果是生成器对象，使用tuple()函数将其转换为元组
print(tuple(t_1))
