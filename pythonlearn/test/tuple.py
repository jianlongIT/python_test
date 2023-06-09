# -*- coding: utf-8 -*-
# Auther : jianlong

c = ({"a": "s", "c": "d"}, {"s", "sda"})
print(id(c))
c[0]["name"] = 'jianlong'
print(c)
d = {"s": "ss", "name": "dqw"}
f = {"s": "ss"}
print(id(c))
print('ss' in d)
print(max(d))
print(min(d))

dict_1 = {"xiaohu": {"record": {"chinese": 98, "english": 96, "math": 99}, "age": 14},
          "yanyan": {"record": {"chinese": 99, "english": 98, "math": 100}, "age": 15}}
print(dict_1)
a = 1024
a **= 3
print(a)

a = [1, 2, 3]
print(a * 2)
print(a)
