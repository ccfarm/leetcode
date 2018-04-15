class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            if s == '':
                return True
            else:
                return False
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or \
                   first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:],p[1:])

s = Solution()
print(s.isMatch("aaa","aa"))