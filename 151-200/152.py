class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        ans = 0
        dp1 = 0
        dp2 = 0
        for x in nums:
            if x >= 0:
                ans = max(ans, dp1 * x)
                dp1 = max(dp1 * x, x)
                dp2 = dp2 * x
            if x < 0:
                ans = max(ans, dp2 * x)
                dp2 = min(dp1 * x, x)
                dp1 = max(dp2 * x, x)
        ans = max(dp1, ans)
        return ans