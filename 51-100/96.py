class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1, 2]
        for i in range(3, n + 1):
            for j in range(1, i + 1):
                f[i] += f[j - 1] * f[i - j]
        return f[n]