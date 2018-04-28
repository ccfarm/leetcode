import collections
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def f(s1, s2, n):
            if n == 1:
                return s1 == s2
            d1 = collections.Counter(s1)
            d2 = collections.Counter(s2)
            if d1 != d2:
                return False
            for i in range(0, n - 1):
                if f(s1[:i], s2[:i], i + 1) and f(s1[i+1:], s2[i+1:], n - i - 1)\
                    or f(s1[:i], s2[n - i - 2:], i + 1) and f(s1[i+1:], s1[:n - i - 2], n - i - 1):
                    return True
            return False
        n = len(s1)
        m = len(s2)
        if n != m:
            return False
        return f(s1,s2, n)