#!/usr/bin/python3
import json
import numpy as np, pandas as pd

setDemo = set(("1", "5", "2"))
setDemo.add("7")

for x in setDemo:
    print("x is value " + x)

setDemo.remove("5")

print("$$$")
for x in setDemo:
    print("x is value " + x)

# 读取数据
# 读json文件
with open('a.json', 'r') as f:
    data = json.load(f)

print("data is start")

print(data)

score = data["score"]

for item in score:
    print(item)
    print("name is " + item["name"])

# 写json 文件

beta = {
    "name": "wang"
}
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(beta, f)

arr1 = np.arange(10)

# print(arr1)
# print(type(arr1))

ssd = {
    "a": 1,
    "b": 7,
    "c": 6

}

s1 = pd.Series(ssd)

print("#####")
print(s1)
print(type(s1))

print("*******")
arr2 = np.array(np.arange(12).reshape(4, 3))
print(arr2)

print("^^^^^")

df1 = pd.DataFrame(arr2)

print(df1)

print("kkk")
# 行标
df1.index = ['q', 'w', 'e', 'r']
print(df1.index)

for a in df1.columns:
    print("a is before")
    print(a)
# 列标
print(df1.columns)
for a in df1.columns:
    print("a is before")
    print(a)

df1.columns = ['one', 'two', 'three']

for a in df1.columns:
    print("a is after")
    print(a)

print(df1)

# 进行sql操作


print("*****")
# 选择指定行
print(df1.loc[["q", "w"], ["one", "two"]])








