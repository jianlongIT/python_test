# -*- coding: utf-8 -*-
# Auther : jianlong

jianlonog = {'name': 'jianlong', 'age': 26}
print(jianlonog.keys())
jianlong_key = list(jianlonog.keys());
print(jianlong_key)

grade_one = {
    "class_1": {"boy": 25, "girl": 22},
    "class_2": {"boy": 21, "girl": 23},
    "class_3": {"boy": 24, "girl": 22},
    "class_4": {"boy": 22, "girl": 22},
    "class_5": {"boy": 20, "girl": 25}
}

keys1 = list(grade_one.keys())
for key1 in keys1:
    print('一年级' + key1[6:] + '班：' + str(grade_one.get(key1)))

print(list(grade_one.values()))

# grade_one.clear()
grade_one.pop('class_1')
del grade_one['class_2']
print(grade_one)