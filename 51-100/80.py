class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        count = 1
        now = nums[0]
        flag = 1
        i = 1
        while i < len(nums):
            # print(now,flag,count)
            if nums[i] != now:
                count += 1
                now = nums[i]
                flag = 1
                i += 1
            elif flag == 1:
                flag += 1
                count += 1
                i += 1
            else:
                del nums[i]
        return count