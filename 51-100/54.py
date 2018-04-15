class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        i = 0
        mm  = m
        nn = n
        while mm >= 2 and nn >= 2:
            for j in range(nn - 1):
                ans.append(matrix[i][i + j])
            for j in range(mm - 1):
                ans.append(matrix[i + j][i + nn - 1])
            for j in range(nn - 1):
                ans.append(matrix[i + mm - 1][i + nn - 1 - j])
            for j in range(mm - 1):
                ans.append(matrix[i + mm - 1 - j][i])
            i += 1
            nn -= 2
            mm -= 2
        if mm == 1:
            for j in range(nn):
                ans.append(matrix[i][i + j])
        elif nn == 1:
            for j in range(mm):
                ans.append(matrix[i + j][i])
        return ans