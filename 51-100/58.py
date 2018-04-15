class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = len(s)
        if s == 0:
            return 0
        else:
            i = l - 1
            while i >= 0 and s[i] != ' ':
                i -= 1
            return l - i - 1
