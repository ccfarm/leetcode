class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 1
        while i >= 1 and nums[i - 1] > nums[i]:
            i -= 1
        if i == 0:
            self.rev(nums, 0, l - 1)
        else:
            index = i
            i -= 1
            j = i + 2
            if j < l:
                index = j
                while j < l:
                    if nums[i] < nums[j] and nums[j] <nums[index]:
                        index = j
                    j += 1
            nums[i], nums[index] = nums[index], nums[i]
            self.rev(nums, i, l)
    def rev(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1