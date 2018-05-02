class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle.copy()
        l = len(triangle)
        for i in range(1, l):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][0]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i,j] = triangle[i][j] + min(dp[i][j-1], dp[i][j])
        ans = 2**31
        for j in range(l+1):
            ans = min(ans, dp[l-1][j])
        return ans