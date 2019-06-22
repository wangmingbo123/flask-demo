import numpy as np, pandas as pd

a = np.arange(8)
print("原始数组")
print(a)
print("\n")

b = a.reshape(4, 2)

print("修改后")

print(b)

s4 = pd.Series(np.array([1, 1, 2, 3, 5, 8]))

print(type(s4.index))

# int 和str互转

print("last val is " + str(s4[5]))
print(s4[5])

list = [1, 3, 7, 3, 6, 6]

# 求最大值和最小值
max = 0
min = 10
for item in list:
    print("item is ", item)
    if (item > max):
        max = item

    if item < min:
        min = item

print("max is ", max)
print("min is ", min)
