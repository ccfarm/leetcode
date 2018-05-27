class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def f(a,b,c,d):
            if a > c:
                a,b,c,d = c,d,a,b
            if b <= c:
                return 0
            else:
                return min(b,d) - c

        return (C-A)*(D-B) + (G-E)*(H-F) -f(A,C,E,G)*f(B,D,F,H)