class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        for k in range(l):
            for i in range(l - k):
                j = i + k
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
        dp2 = [[0] * l]
        for i in range(l):
            if dp[0][i]:
                dp2[i] = 0
            else:
                for k in range(i):
                    dp2[0][k] = min(dp2[0][k], dp2[0][k] + dp2[k+1][i])
        return dp2[0][l-1]