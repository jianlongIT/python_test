# -*- coding: utf-8 -*-
# Auther : jianlong
import copy

a = [[1, 2], [2, 3]]
b = copy.deepcopy(a)
print(b)
b[0].append(4)
print(a)
print(b)

c = a.copy();
c[0].append(5)
print(a)

test = []
test.extend('abcd', )
print(test)

test1 = [1, 3, 7, 9]
test2 = [2, 2, 6, 8]
test1.extend(test2)
test1.sort()
print(test1)
test1[2:5] = 's', 's', '2'
print(test1)

code = ["e_ying", "d_shi", 6, "a_wo", 1, 2, 3, "f_xiong", "b_men", 4, 5, "c_dou"]
# 定一个空列表crack 放入字符串
crack = ['a']

# 定义一个空列表number 放入数字
number = [1]

# 使用append将code里面的字符串根据索引添加到crack列表中
for c in code:
    if type(c) is str:
        crack.append(c)
    if type(c) is int:
        number.append(c)

print('crack', crack)
print('number', number)
crack.sort()
number.sort()

print("数字添加完成", number)

new_code = code.copy()
code.clear()
print("复制原编码", new_code)

print("清空原列表编码", code)

name = 'jianlong'
name = name[::-1]
print(name)
jianlong = []
jianlong.extend(name)
jianlong.reverse()

print(jianlong)

file_neme = 'file_path = "F:\imoocProjects\askDemo\imooc\demo.py"';
print(file_neme.rindex('"'))
print(file_neme.rindex('\\'))
print(file_neme[43:50])
cert_no = '422123199102020304'
print(cert_no[6:14])

new_name = "JianLong"
lower_name = new_name.lower()
print(lower_name[0:4].capitalize() + lower_name[4:].capitalize())
print(lower_name[0:4] + '_' + lower_name[4:])

books_dict = {
    "classical": ["三国演义", "西游记", "红楼梦", "水浒传"],
    "morden": ["呐喊", "彷徨", "朝花夕拾", "春水", "繁星", "边城"],
    "science": ["流浪地球", "宇宙往事", "三体", "死神永生"]
}
books_dict["science"].append('沙丘')
books_dict["morden"].append('海地两万里')

print(len(books_dict["classical"])+len(books_dict["morden"])+len(books_dict["science"]))
