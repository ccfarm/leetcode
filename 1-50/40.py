class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        for i in range(len(candidates)):
            for j in reversed(range(target + 1)):
                if j == candidates[i]:
                    dp[j].append([candidates[i]])
                elif j > candidates[i] and len(dp[j - candidates[i]]) > 0:
                    for l in dp[j - candidates[i]]:
                        ll = l.copy()
                        ll.append(candidates[i])
                        dp[j].append(ll)
        ans = []
        s = set([])
        for i in range(len(dp[target])):
            x = dp[target][i]
            x = list(map(str(item) for item in x))
            st = ''.join(x)
            if st not in s:
                s.add(st)
                ans.append(x)
        return ans
