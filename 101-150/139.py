class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set()
        l1 = 0
        l2 = 2 ** 32
        for word in wordDict:
            wordSet.add(word)
            l = len(word)
            l1 = min(l1, l)
            l2 = max(l2, l)
        l = len(s)
        dp = [False] * l
        for i in range(l1-1, l):
            for j in range(max(0, i - l2 + 1), i - l1 + 1):
                if j == 0:
                    dp[i] = dp[i] or s[:i+1] in wordSet
                else:
                    dp[i] = dp[i] or (dp[j-1] and s[j:i+1] in wordSet)
        return dp[l]