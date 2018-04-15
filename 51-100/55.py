class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        f = nums[0]
        l = len(nums)
        i = 0
        if f >= l - 1:
            return True
        while 1:
            ff = 0
            while i < f:
                i += 1
                ff = max(ff, nums[i] + i)
            if f == ff:
                return False
            f = ff
            if f >= l - 1:
                return True