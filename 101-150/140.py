class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
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
        dp = {}
        def dfs(i):
            dp[i] = []
            for k in range(l1, l2):
                j = i + k
                if j <= l:
                    if s[i:j] in wordSet:
                        if j  < l:
                            if j not in wordSet:
                                dfs(j)
                            for x in dp[j]:
                                dp[i].append(s[i:j] + x)
                        else:
                            dp[i].append(s[i:j])
            print(i, dp[i])
        dfs(0)
        return dp[0]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wl = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
a = Solution
print(a.wordBreak(a, s, wl))