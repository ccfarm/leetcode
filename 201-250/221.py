class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        ans = 0
        dp0 = [[0 for y in range(m)] for n in range(n)]
        dp1 = [[0 for y in range(m)] for n in range(n)]
        dp2 = [[0 for y in range(m)] for n in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if j > 0:
                        dp1[i][j] = dp1[i][j-1] + 1
                    else:
                        dp1[i][j] = 1
                    if i > 0:
                        dp2[i][j] = dp2[i-1][j] + 1
                    else:
                        dp2[i][j] = 1
                    dp0[i][j] = min(dp1[i][j], dp2[i][j])
                    if i > 0 and j > 0:
                        tmp = dp0[i-1][j-1] + 1
                    else:
                        tmp = 1
                    dp0[i][j] = min(dp0[i][j], tmp)
                    ans = max(ans, dp0[i][j])
        return ans ** 2
