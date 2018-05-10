class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = [26]
        sum = 26
        while sum < n:
            l.append(l[-1] * 26)
            sum += l[-1]