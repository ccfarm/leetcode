class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        s2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        s3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        s4 = ["", "M", "MM", "MMM"]
        sum = 0
        if "CM" in s:
            sum -= 200
        if "CD" in s:
                sum -= 200
        if "XC" in s:
            sum -= 20
        if "XL" in s:
            sum -= 20
        if "IX" in s:
            sum -=2
        if "IV" in s:
            sum -=2
        sum += s.count('M') * 1000
        sum += s.count('D') * 500
        sum += s.count('C') * 100
        sum += s.count('L') * 50
        sum += s.count('X') * 10
        sum += s.count('V') * 5
        sum += s.count('I') * 1
        return sum
s = Solution()
print(s.romanToInt("MCMLXXXIV"))