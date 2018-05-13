class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        m = 1
        while s != '':
            c = s[-1]
            ans += m * (ord(c) - ord('A'))
            m *= 26
            s = s[:-1]
        return ans