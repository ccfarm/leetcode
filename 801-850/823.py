class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = 10 ** 9 + 7
        n = len(A)
        dp = [1] * n
        A.sort()
        d = {}
        for i in range(n):
            d[A[i]] = i
        for i in range(n):
            for j in range(i):
                if A[j] ** 2 > A[i]:
                    break
                elif A[j] ** 2 == A[i]:
                    dp[i] += dp[j]
                    dp[i] = dp[i] % m
                elif A[j] ** 2 < A[i] and A[i] % A[j] == 0 and A[i] // A[j] in d:
                    dp[i] += 2 * dp[j] * dp[d[A[i] // A[j]]]
                    dp[i] = dp[i] % m
        ans = 0
        for i in range(n):
            ans += dp[i]
            ans %= m
        return ans