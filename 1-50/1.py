class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = set(nums)
        for i in range(len(nums)):
                if target - nums[i] in s:
                    if nums[i] != target // 2:
                        return(i, nums.index(target - nums[i]))
                    elif nums.count(nums[i]) > 1:
                        return(i,nums.index(nums[i], i+1))