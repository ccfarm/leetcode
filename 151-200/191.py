class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [0] * 32
        i = 0
        ans = 0
        while n > 0:
            b[i] = n % 2
            n //= 2
            if b[i] == 1:
                ans += 1
            i += 1
        return ans