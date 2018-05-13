class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        stack = []
        for x in nums:
            if stack == [] or stack[-1] == x:
                stack.append(x)
            else:
                del stack[-1]
        return stack[-1]