class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        pro = self.kthGrammar(N - 1, (K - 1) // 2 + 1)
        odd = K % 2
        if pro == 0:
            if odd == 1:
                ans = 0
            else:
                ans = 1
        else:
            if odd == 1:
                ans = 1
            else:
                ans = 0
        #print(N, K, ans)
        return ans
a = Solution()
print(a.kthGrammar(1,1))
print(a.kthGrammar(2,1))
print(a.kthGrammar(2,2))
print(3,1,a.kthGrammar(3,1))
print(3,2,a.kthGrammar(3,2))
print(3,3,a.kthGrammar(3,3))
print(3,4,a.kthGrammar(3,4))
print(a.kthGrammar(4,5))