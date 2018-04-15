class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        while "**" in p:
            p = p.replace("**", "*")
        n = len(s)
        m = len(p)
        i = 0
        j = 0
        ii = -1
        jj = -1
        while i < n:
            if j < m and s[j] == '*':
                ii = i
                jj = j = j + 1
            elif j < m and (s[i] == s[j] or s[j] == '.'):
                i += 1
                j += 1
            elif ii >= 0:
                ii = i = ii + 1
                j = jj
            else:
                return False
        while j < m:
            if p[j] != '*':
                return False
            j += 1
        return True
