class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        l = len(A)
        if l != len(B):
            False
        for i in range(l - 1):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False