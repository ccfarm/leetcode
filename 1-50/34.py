class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        first = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target and (m == 0 or nums[m - 1] < target):
                first = m
                break
            else:
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
        if first == -1:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target and (m == len(nums) - 1 or nums[m + 1] > target):
                last = m
                break
            else:
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return [first, last]