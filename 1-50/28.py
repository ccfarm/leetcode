class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        n = len(haystack)
        m = len(needle)
        next = [0 for x in range(m)]
        next[0] = -1
        i = 0
        j = 1
        while j < m - 1:
            if needle[j] == needle[i]:
                next[j + 1] = i + 1
                i += 1
                j += 1
            else:
                i = next[i]
                if i == -1:
                    i = 0
                    j += 1
        print(next)
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                if j == m - 1:
                    return i - m + 1
                i += 1
                j += 1
            else:
                j = next[j]
                if j == -1:
                    i += 1
                    j = 0
        return -1

s = Solution()
print(s.strStr("aabaaabaaac", "aabaaac"))