class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])
        best = 0
        for i in range(2*n-1):
            for j in range(2*m-1):
                if A[i][j] == 1:
                    ans = 0
                    d1 = i - n + 1
                    d2 = j - m + 1
                    for i1 in range(n):
                        if (i - d1)>=0 and (i - d1)<n:
                            for j1 in range(m):
                                if (j - d2)>=0 and (j-d2)<m:
                                    if B[i1][j1] == 1:
                                        ans += 1
                    best = max(best, ans)
        return best