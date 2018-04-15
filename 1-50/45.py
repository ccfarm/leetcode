class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        f = nums[0]
        step = 1
        l = len(nums)
        i = 0
        if f >= l - 1:
                return step
        while 1:
            ff = 0
            while i < f:
                i += 1
                ff = max(ff, nums[i] + i)
            step += 1
            f = ff
            if f >= l - 1:
                return step