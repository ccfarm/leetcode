class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        dp = [[False] * (l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                k = i + j
                if k == 0:
                    dp[i][j] == True
                if i < l1 and s1[i] == s3[k]:
                    dp[i+1][j] = dp[i][j] or dp[i+1][j]
                if j < l2 and s2[j] == s3[k]:
                    dp[i][j+1] = dp[i][j] or dp[i][j+1]
        return dp[l1][l2]

