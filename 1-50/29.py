class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2 ** 32 -1
        sign = 1
        if dividend < 0:
            dividend *= -1
            sign *= -1
        if divisor < 0:
            divisor *= -1
            sign *= -1
        now = divisor
        count = 1
        l1 = []
        l2 = []
        while now <= dividend:
            l1.append(now)
            l2.append(count)
            now += now
            count += count
        ans = 0
        for i in reversed(range(len(l1))):
            if l1[i] <= dividend:
                ans += l2[i]
                dividend -= l1[i]
        return ans
