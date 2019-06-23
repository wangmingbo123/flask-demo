#!/usr/bin/python3
import requests

print("hello world")

list1 = [1, 2, 5, 2]

print(list1[1:])

for x in list1:
    print("x is end=")
    print(x)

dict = {
    "name": "wang",
    "age": 19
}

print("#####")
print(dict['name'])
print("#####")

for key in dict.keys():
    print("&&&")
    print("key is " + key)
    print(dict[key])
    print("&&&")

# 遍历元祖
for item in dict.items():
    print("item is begin")
    print(item)
    print(item[0])
    print(item[1])
    print("item is end")

a = [(1, 2), (8, 9)]

print(a)
print(a.pop(0))

a.append((2, 3))

print(a)
