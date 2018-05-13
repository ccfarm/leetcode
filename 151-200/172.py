class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        tmp = 5
        while n // tmp > 0:
            ans += n // tmp
            tmp *= 5
        return ans