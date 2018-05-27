class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        roof = 2 ** 31
        l = len(S)
        f = []
        for i in range(1,11):
            if i < l-2 and int(S[:i]) < roof:
                for j in range(i+1, i+11):
                    if j < l-1 and int(S[i:j]) < roof:
                        f = [int(S[:i]), int(S[i:j])]
                        kk = j
                        while kk < l:
                            temp = f[-1] + f[-2]
                            ts = str(temp)
                            ll = len(ts)
                            if kk + ll <= l and ts == S[kk: kk+ll]:
                                f.append(temp)
                            kk += ll
                        if kk == l:
                            return f
        return []