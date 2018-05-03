class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0] * 32
        b = [0] * 32
        for x in nums:
            if x > 0:
                i = 0
                while x > 0:
                    a[i] += x % 2
                    i += 1
                    x /= 2
            else:
                x = -x
                i = 0
                while x > 0:
                    b[i] += x % 2
                    i += 1
                    x /= 2

        ans = 0
        i == 0
        while i < 32:
            ans += (a[i] % 3 * 2 ** i)
            i += 1
        if ans == 0:
            i = 0
            while i < 32:
                ans += (b[i] % 3 * 2 ** i)
                i += 1
            ans = -ans
        return ans