class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0] * m] * n

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] == i
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                    if word1[i] == word2[j]:
                        q = 0
                    else:
                        q = 1
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + q)
        return dp[n-1][m-1]