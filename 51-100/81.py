class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums == []:
            return False
        i = len(nums) - 1
        count = 0
        while nums[i] <= nums[0]:
            x = nums.pop()
            nums.insert(0,x)
            count += 1
            if count > len(nums):
                break

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        return False