class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        i = 0
        j = len(nums) - 1
        while i < j and nums[i] == nums[j]:
            del nums[j]
            j -= 1
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            else:
                if nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m