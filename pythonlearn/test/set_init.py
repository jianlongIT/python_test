# -*- coding: utf-8 -*-
# Auther : jianlong
from collections import Counter

alist = [147796, 155613, 993659, 162337, 167688, 170246, 175728, 179076, 181690, 182498, 185027, 185988, 187355, 189649,
         208818, 213415, 213730, 689093, 215574, 219052, 227969, 237532, 244536, 248343, 402240, 253964, 255151, 258282,
         263072, 269725, 273998, 312746, 402240, 429807, 291034, 185027, 303643, 306282, 312746, 322205, 322947, 378521,
         323567, 185027, 189649, 327307, 328015, 147796, 331208, 355153, 147796, 356382, 357030, 371721, 371881, 372905,
         914931, 378521, 386644, 387300, 389827, 391957, 392603, 893962, 403005, 387300, 624877, 408995, 189649, 312746,
         416183, 417681, 422329, 429807, 378521, 433060, 312746, 438597, 444267, 453494]
print(len(alist))
adict = Counter(alist)
print(adict)
print(type(adict))

aset = set(alist)

print(len(aset))

print('aset', aset)
aset.clear()
dict = ('python',)
aset.update(('python',))
aset.update(('python',), ('python',))
print(aset)

adic = (1, 1, 1, 23, 4, 51)
aset2 = set(adic)
print(aset2)

bset = {'java'}
result1 = aset.difference(bset)
print(result1)
result2 = aset.intersection(bset)
print(result2)
result3 = aset.union(bset)
print(result3)

int1 = int(' 2')
print(int1, type(int1))

sdict = ('1', '22', '3')
print('|'.join(sdict))

s = 'gasdwfafas'
print(sorted(s))
