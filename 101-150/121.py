class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre = sys.maxint
        ans = 0
        for x in prices:
            ans = max(ans, x - pre)
            pre = min(pre, x)
        return ans