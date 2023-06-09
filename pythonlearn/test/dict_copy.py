# -*- coding: utf-8 -*-
# Auther : jianlong

fruits = {
    'apple': 50,
    'pear': 60,
    'hamimelon': '100'
}

print(fruits)
real_fruits = fruits.copy()

real_fruits['banana'] = '10'
real_fruits.update({"cherry": 20})
print(real_fruits)
print('pear' in real_fruits)
print(bool(real_fruits.get('pear1')))
real_fruits['pear']

last = real_fruits.popitem()
print(last)

real_fruits.pop('apple')

print(real_fruits)

print('apple' == 'apple')
print('----------------------------------------')
print(bool(not None))

aset = {'1'}
print(type(aset))
