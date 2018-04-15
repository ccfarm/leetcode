class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            while nums[i] > 0 and nums[i] <= l:
                j = nums[i] - 1
                nums[j] ,nums[i] = nums[i], nums[j]
        ans = l + 1
        for i in range(l):
            if nums[i] != i + 1:
                ans = i + 1
                break
        return ans
