class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        now = 0
        for i in range(len(nums)):
            now = max(now + nums[i], nums[i])
            ans = max(ans, now)
        return ans