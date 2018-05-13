class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a = []
        ml = 0
        for x in nums:
            s = str(x)
            a.append(s)
            ml = max(ml, len(s))
        for i in range(a):
            a[i] = a[i] + '/' * (ml - len(a[i]))
        a.sort(reverse=True)
        ans = ''.join(a).replace('/', '')
        return ans