class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if nums == [] or nums[0] > target:
            return 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target and (m == len(nums) - 1 or nums[m + 1] >= target):
                return m + 1
                break
            else:
                if nums[m] > target:
                    r = m - 1
                else:
                    l = l + 1