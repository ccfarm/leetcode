class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0 and digits[i] >= 10:
            if i == 0:
                digits[0] %= 10
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
                digits[i] %= 10
            i-= 1
        return digits