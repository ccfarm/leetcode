class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        dp = nums.copy()
        for i in range(2, l):
            tmp = dp[i-2]
            if i - 3 >= 0:
                tmp = max(tmp, dp[i-3])
            dp[i] = nums[i] + tmp
        ans = dp[-1]
        if l > 1:
            ans = max(ans, dp[-2])
        return ans