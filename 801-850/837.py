class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0.0] * (K + W)
        for k in range(K, N+1):
            dp[k] = 1.0
        S = min(N-K+1, W)
        for k in range(K-1, -1, -1):
            dp[k] = S / W
            S = S - dp[k + W] + dp[k]
        return dp[0]