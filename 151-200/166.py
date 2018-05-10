class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = 1
        if numerator < 0:
            a = -numerator
            flag *= -1
        else:
            a = numerator
        if denominator < 0:
            b = -denominator
            flag *= -1
        ans = str(a//b)
        a = a % b
        l = []
        while a * 10 // b not in l:
            l.append(a * 10 // b)
            a = a * 10 % b
        index = l.index(a * 10 // b)
        l.insert(index, '(')
        l.append(')')
        l.insert(0, '.')
        ans = ans + ''.join(l)
        return ans

