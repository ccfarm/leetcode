class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        size = []
        min_len = 2**32
        for j in range(len(strs)):
            size.append(len(strs[j]))
            min_len = min(len(strs[j]), min_len)
        for i in range(min_len + 1):
            s = strs[0][:i]
            #print(s)
            for j in range(1, len(strs)):
                if (s != strs[j][:i]):
                    print(s, strs[j][:i])
                    return s[:i - 1]
            if i == min_len:
                return s

s = Solution()
print(s.longestCommonPrefix([""]))