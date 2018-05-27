class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        i = 0
        j = 0
        while j < k and j < len(nums):
            index = nums[j] // (t + 1)
            if index in d:
                return True
            if index-1 in d and nums[j] - d[index-1] <= t:
                return True
            if index+1 in d and d[index+1] - nums[j] <= t:
                return True
            d[index] = nums[j]
            j += 1
        while j < len(nums):
            index = nums[i] // (t + 1)
            d.pop(index)
            i += 1
            index = nums[j] // (t + 1)
            if index in d:
                return True
            if index - 1 in d and nums[j] - d[index - 1] <= t:
                return True
            if index + 1 in d and d[index + 1] - nums[j] <= t:
                return True
            d[index] = nums[j]
            j += 1
        return False