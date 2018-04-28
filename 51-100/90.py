class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        nums.sort()
        ans = []
        now = []
        def dfs(i):
            if i == len(nums):
                ans.append(now.copy())
            else:
                dfs(i + 1)
                now.append(nums[i])
                dfs(i + 1)
                now.pop()
        dfs(0)
        return ans
