class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        now = []
        def dfs(start, k):
            if k == 0:
                ans.append(now.copy())
            else:
                for i in range(start, n + 2 - k):
                        now.append(i)
                        dfs(i + 1, k - 1)
                        now.pop()
        dfs(1, k)
        return ans
