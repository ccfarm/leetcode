class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        i = 0
        j = 0
        while j < k:
            if nums[j] in s:
                return True
            s.add(nums[j])
            j += 1
        while j < len(nums):
            s.remove(nums[i])
            i += 1
            if nums[j] in s:
                return True
            s.add(nums[j])
            j += 1
        return False