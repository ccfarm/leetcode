class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return max(n, m)
        dp = [[0 for y in range(m + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                    if word1[i - 1] == word2[j - 1]:
                        q = 0
                    else:
                        q = 1
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + q)
        return dp[n][m]
