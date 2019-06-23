class Solution:
    def searchMatrix(self, matrix, target):
        if 0 == len(matrix) or 0 == len(matrix[0]):
            return False
        hang, lie = len(matrix), len(matrix[0])
        i = 0;
        j = lie - 1
        while i < hang and j >= 0:
            item = matrix[i][j]
            if target == item:
                return True
            elif target < item:
                j = j - 1
            else:
                i = i + 1
        return False
