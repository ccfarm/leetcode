class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp = dungeon
        n = len(dp)
        m = len(dp[0])
        i = n-1
        j = m-2
        while True:
            if j < 0:
                j = m-1
                i -= 1
                if i < 0:
                    break
            dp[i][j] = 0
            if j+1 < m:
                dp[i][j] = max(dp[i][j+1], dp[i][j])
            if i+1 < n:
                dp[i][j] = max(dp[i+1][j], dp[i][j])
            dp[i][j] = min(dp[i][j], 0)
        return -dp[0][0]
