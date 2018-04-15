class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        ans = []
        s = set([])
        n = len(nums)
        def dfs(d):
            if d > n:
                ans.append(l.copy())
            else:
                for num in nums:
                    if num not in s:
                        s.add(num)
                        l.append(num)
                        dfs(d + 1)
                        l.remove(num)
                        s.remove(num)
        dfs(1)
        return ans