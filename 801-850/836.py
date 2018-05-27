class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def f(a,b,c,d):
            if a > c:
                a,b, c,d =c,d,a,b
            return not (b <= c)
        ans = f(rec1[0], rec1[2], rec2[0], rec2[2]) and f(rec1[1], rec1[3], rec2[1], rec2[3])
        return ans
