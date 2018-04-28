class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            if m ** 2 <= x and (m + 1) ** 2 > x:
                return m
            elif m ** 2 <= x:
                l = m + 1
            else:
                r = m - 1