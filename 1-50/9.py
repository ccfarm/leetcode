class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x % 10 == 0:
            return False
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
            if rev == x or rev // 10 == x:
                return True
        return False

s = Solution()
print(s.isPalindrome(1212))