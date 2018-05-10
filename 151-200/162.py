class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        size = len(nums)
        if size == 1:
            return 0
        r = size - 1
        while l < r:
            m = (l + r) // 2
            if m > 0 and m < size-1:
                if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                    return m
                elif nums[m] < nums[m+1]:
                    l = m + 1
                elif nums[m] < nums[m-1]:
                    r = m - 1
            elif m > 0:
                if nums[m] > nums[m-1]:
                    return m
                else:
                    r = m - 1
            elif m < size - 1:
                if nums[m] > nums[m+1]:
                    return m
                else:
                    l = m + 1
        return 0
