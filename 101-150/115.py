class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        dp = [[0] * ls for x in range(lt)]
        for i in range(ls):
            for j in range(lt):
                if j == 0:
                    if i == 0:
                        if s[i] == t[j]:
                            dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j]
                        if s[i] == t[j]:
                            dp[i][j] += 1
                elif i >= j:
                    dp[i][j] = dp[i-1][j]
                    if s[i] == t[j]:
                        dp[i][j] += dp[i-1][j-1]
        return dp[ls][lt]
