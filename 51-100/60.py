class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = [1]
        for i in range (1, n):
            a[i] = a[i] * (i + 1)
        l = [x for x in range(1, n + 1)]
        i = n
        ans = ""
        while i > 1:
            ans = ans + str(l[k // a[i - 2]])
            k %= a[i - 2]
            i -= 1
        ans = ans + str(l[0])
        return ans