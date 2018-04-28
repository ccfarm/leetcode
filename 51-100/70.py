class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        a = 1
        b = 1
        n -= 2
        while n >= 0:
            n -= 1
            b, a = a + b, b
        return b