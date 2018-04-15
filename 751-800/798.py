class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        d = {}
        d[1] = 0
        for i in range(n * 3):
            d[-i] = 0
        for i in range(n):
            dis = A[i] - i
            if dis > 1:
                dis = 1
            d[dis] += 1
        best = 2**32
        ans = 0
        for i in range(n):
            print(n - d[1])
            if best > d[1]:
                best = d[1]
                ans = i
            x = A[i] - i
            if x <= -i:
                d[x] -= 1
            else:
                d[1] -= 1
            dis = A[i] - n + 1 - i - 1
            d[dis] += 1
            d[1] += d[-i]
        return ans
