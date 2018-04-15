class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        s2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        s3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        s4 = ["", "M", "MM", "MMM"]

        ans = []
        ans.append(s1[num % 10])
        num //= 10
        ans.append(s2[num % 10])
        num //= 10
        ans.append(s3[num % 10])
        num //= 10
        ans.append(s4[num % 10])
        ans.reverse()
        return ''.join(ans)
s = Solution()
print(s.intToRoman(1666))