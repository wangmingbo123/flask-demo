#!/usr/bin/python3
import json
import numpy as np, pandas as pd

listA = [1, 2, 5]
listB = [0, 3, 9]
last = []

a = 0
b = 0

print(listA[a])

while a < len(listA) and b < len(listB):

    if (listA[a] < listB[b]):
        last.append(listA[a])
        a = a + 1
    else:
        last.append(listB[b])
        b = b + 1

while a < len(listA):
    last.append(listA[a])
    a = a + 1

while b < len(listB):
    last.append(listB[b])
    b = b + 1

print("flask demo ")

print(last)

# 二分查找


with open("a.json", "r") as f:
    data = json.load(f)

print("data type", type(data))
# print(data["a"])
compareData = data["a"]

print("compare is", type(compareData))

low = 0;
high = len(last) - 1;

# 没有找到，默认是-1
findIndex = -1;

while low < high:
    mid = int((low + high) / 2)
    if (last[mid] == compareData):
        findIndex = mid
        break

    if (compareData < mid):
        high = mid - 1
    else:
        low = mid + 1

print("mid is ", mid)
print("index is ", findIndex)
