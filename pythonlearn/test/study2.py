# -*- coding: utf-8 -*-
# Auther : jianlong
b = "python"


def pr():
    print(b)


pr()

trmp = ""
index = 0


def getstr(str):
    global index
    global trmp
    for s in str:
        if (index == 0):
            trmp = s.upper()
        else:
            trmp += s
        index += 1
    print(trmp)


getstr("jianlong")


def args(a, b, *args):
    print(a, b, *args)


q = 1
w = 2
s = (1, 2)

print(*s)

args(q, w, *s)


def func1(a, b, c):
    print(a, b, c)


s = (1, 2, 3)
func1(*s)

i = 1
result = 1


def getnum(n):
    global result
    global i
    if i > n:
        return result
    else:
        result *= i
        i += 1
        return getnum(n)


sum = getnum(5)

print('结果', sum)

f1 = lambda a: print("lambda =", a)
f1("word")
f1("word")

list1 = [1, 2, 3, 4, 5, 6, 4, 1]
list1.sort(reverse=False)
print(list1)

f3 = lambda x: 3.14 * x * x

print(f3(2))

students = {
    1: {
        "name": "jianlong",
        "age": 27
    }
}

print(students.get(1).get("name"))

print(students.get(1).keys())
print(tuple(students.get(1).keys()))

set1 = {1, 2, 3}
set2 = {4, 5, 6, 7}
set3 = set.union(set1, set2)
print(set3)
