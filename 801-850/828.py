import collections
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        d = {}
        for i,c in enumerate(S):
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
        ans = 0
        for l in d.values():
            tmp = [-1] + l + [len(l)+1]
            for i in range(1, len(tmp) - 1):
                left = tmp[i] - tmp[i-1]
                right = tmp[i+1] - tmp[i]
                ans += left * right
        return ans
