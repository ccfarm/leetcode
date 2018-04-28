class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for y in range(n)] for x in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0 and (i == 0 or dp[i - 1][0] == 1):
                dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 0 and (i == 0 or dp[0][i - 1] == 1):
                dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m - 1][n - 1]
