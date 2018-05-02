class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        for k in range(l):
            for i in range(l - k):
                j = i + k
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
        ans = []
        tmp = []
        def dfs(i):
            if i >= l:
                ans.append(tmp.copy())
            else:
                for j in range(i, l):
                    if dp[i][j]:
                        tmp.append(s[i : j + 1])
                        dfs(j + 1)
                        tmp.pop()
        dfs(0)
        return ans