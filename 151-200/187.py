from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = [s[i:i+10] for i in range(len(s)) if i+10 <= len(s)]
        d = Counter(l)
        ans = [x for x in d.keys() if d[x] >1]
        return ans
