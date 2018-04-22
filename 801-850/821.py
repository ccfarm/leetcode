class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = len(S)
        al = [-1] * l
        ar = [-1] * l
        r = -1
        for i in range(l):
            if S[i] == C:
                al[i] = 0
                ar[i] = 0
                j = i - 1
                while j >=0 and S[j] == -1:
                    al[j] = j - i
                    j -= 1
                k = 1
                while r != -1 and r < i:
                    ar[r] = k
                    r += 1
                    k += 1
                r = i + 1
        k = 1
        while r != -1 and r < l:
            ar[r] = k
            r += 1
            k += 1
        for i in range(l):
            al[i] = min(al[i], ar[i])
        return al