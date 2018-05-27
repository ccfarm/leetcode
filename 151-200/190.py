class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = [0] * 32
        i = 0
        while n > 0:
            b[i] = n % 2
            n //= 2
        m = 2 ** 31
        i = 0
        ans = 0
        while i < 32:
            ans += b[i] * m
            m //= 2
        return ans
