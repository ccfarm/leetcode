class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = 2 ** 31
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10
        ans *= sign
        if ans >= limit - 1 or ans <= -1 * limit:
            return 0
        else:
            return ans

s = Solution()
print(s.reverse(-1230))