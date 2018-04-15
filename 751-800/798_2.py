class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        bad = [0] * n
        for i, x in enumerate(A):
            left = (i - x + 1) % n
            right = (i + 1) % n
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1
        cur = 0
        ans = 0
        best = 0
        for i, x in enumerate(bad):
            cur += bad[x]
            if cur > best:
                best = cur
                ans = i
        return ans