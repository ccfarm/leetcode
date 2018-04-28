import collections
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)
        i = I = J = 0
        for j, x in enumerate(s, 1):
            if x in need:
                missing -= need[x] > 0
                need[x] -= 1
                if missing == 0:
                    while s[i] not in need or need[s[i]] < 0:
                        if s[i] in need:
                            need[s[i]] += 1
                        i += 1
                    if J == 0 or j - i < J - I:
                        J = j
                        I = i
        return s[I:J]