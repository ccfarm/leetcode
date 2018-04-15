class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[]for _ in range(target + 1)]
        for i in range(len(candidates)):
            for j in range(target + 1):
                if j == candidates[i]:
                    dp[j].append([candidates[i]])
                elif j > candidates[i] and len(dp[j - candidates[i]]) > 0:
                    for l in dp[j - candidates[i]]:
                        ll = l.copy()
                        ll.append(candidates[i])
                        dp[j].append(ll)
        return dp[target]