import numpy as np, pandas as pd


def searchMatrix(matrix, target):
    if 0 == len(matrix) or 0 == len(matrix[0]):
        return False
    hang, lie = len(matrix), len(matrix[0])
    i = 0;
    j = lie - 1

    while i < hang and j >= 0:
        if target == matrix[i][j]:
            return True
        mm = np.array(matrix)
        # (1,j) 无需包括该元素
        #  走下面的列
        if search(mm[i, 0:j], target) or search(mm[i:hang, j], target):
            return True

        i = i + 1
        j = j - 1
    return False


def search(list: list, target):
    return target in list


m = list([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]])

mm = np.array(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
)
print(searchMatrix(m, 16))

# 第一列
# print(mm[1:2, 1])

# 第一行
# print(mm[1, ...])
