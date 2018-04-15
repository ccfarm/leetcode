class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        max = 2 ** 31 - 1
        min = - 2 ** 31
        l = [str(x) for x in range(10)]
        digit = l[:]
        l.append('-')
        l.append('+')
        ans = 0
        s = s.strip()
        if s == '' or s[0] not in l:
            return 0
        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            sign = -1
        if s == '' or s[0] not in digit:
            return 0
        for i in range(len(s)):
            if s[i] in digit:
                ans *= 10
                ans += int(s[i])
            else:
                break
        ans *= sign
        if ans > max:
            ans = max
        elif ans < min:
            ans = min
        return ans

s = Solution()
print(s.myAtoi("  -0012a42"))