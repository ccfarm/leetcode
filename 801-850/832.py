class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        m = len(A[0])
        for i in range(n):
            l = 0
            r = m - 1
            while l < r:
                A[i][l], A[i][r] = A[i][r], A[i][l]
                l += 1
                r -= 1
        for i in range(n):
            for j in range(m):
                A[i][j] = 1-A[i][j]
        return A
