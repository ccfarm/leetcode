class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        ans = []
        s = set([])
        s2 = set([])
        n = len(nums)
        def dfs(d):
            if d > n:
                st = ''.join(list(map(lambda x: str(x),l)))
                if st not in s2:
                    s2.add(st)
                    ans.append(l.copy())
            else:
                for i in range(n):
                    if i not in s:
                        s.add(i)
                        l.append(nums[i])
                        dfs(d + 1)
                        l.pop()
                        s.remove(i)
        dfs(1)
        return ans
s = Solution()
print(s.permute([1,1,5]))