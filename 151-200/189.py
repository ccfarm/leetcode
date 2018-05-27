class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k > l:
            k %= l
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)