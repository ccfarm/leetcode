class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        postive = set([])
        negtive = set([])
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0:
                negtive.add(nums[i])
            elif nums[i] > 0:
                postive.add(nums[i])
        zeros =  nums.count(0)
        if zeros >= 3:
            ans.append([0, 0, 0])
        if zeros >= 1:
            for x in negtive:
                if -x in postive:
                    ans.append([x, 0, -x])
        for x in negtive:
            if nums.count(x) >= 2 and -2 * x in postive:
                ans.append([x, x, -2 * x])
            if x % 2 == 0 and -x // 2 in postive and nums.count(-x // 2) >= 2:
                    ans.append([x, -x // 2 , -x // 2])
        for x in negtive:
            for y in negtive:
                if x < y and -(x + y) in postive:
                    ans.append([x, y, -(x + y)])
        for x in postive:
            for y in postive:
                if x < y and -(x + y) in negtive:
                    ans.append([-(x + y), x, y])
        return ans