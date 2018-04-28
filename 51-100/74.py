class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        nn = (n + 1) * (m + 1) - 1
        l = 0
        r = nn
        while l <= r:
            mm = (l + r) // 2
            i = mm // n
            j = mm % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mm - 1
            else:
                l = mm + 1
        return False
