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
        from functools import cmp_to_key
        a.sort(key=cmp_to_key(lambda x,y:int(y+x)-int(x+y)))
        print(a)
        ans = ''.join(a).lstrip('0')



        return ans or '0'