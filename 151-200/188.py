class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if k > len(prices) // 2:
            ans = 0
            for i in range(len(prices)-1):
                if prices[i] < prices[i+1]:
                    ans += prices[i+1] - prices[i]
            return ans

        b = [-2**32] * k
        s = [0] * k
        for x in prices:
            s[0] = max(s[0], b[0] + x)
            b[0] = max(b[0], -x)
            for i in range(1,k):
                s[1] = max(s[i], b[i] + x)
                b[i] = max(b[i], s[i-1] - x)
        return s[k-1]