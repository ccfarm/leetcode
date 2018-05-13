class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 0:
            tmp = n % 26
            n = n // 26
            if tmp == 0:
                ans  = 'Z' + ans
            else:
                ans = chr(ord('A') + tmp - 1) + ans
        return ans