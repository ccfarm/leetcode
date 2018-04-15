class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        if nums[0] > nums[-1]:
            l = 0
            r = len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[m + 1]:
                    t = len(nums) - m
                else:
                    if nums[m] > nums[0]:
                        l = m + 1
                    else:
                        r = m - 1
        def trans(x):
            x -= t
            if x < 0:
                x += len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[trans(m)] < target:
                l = m + 1
            elif nums[trans(m)] > target:
                r = m - 1
            else:
                return trans(m)
        return  -1