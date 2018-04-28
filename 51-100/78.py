class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        ans = []
        now = []
        def dfs(k):
            if k  >= l:
                ans.append(now.copy())
            else:
                dfs(k + 1)
                now.append(nums[k])
                dfs(k + 1)
                now.pop()
        dfs(0)
        return ans