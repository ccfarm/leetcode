class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s1 = S[1:-1]
        ans = []
        def fun(n):
            r = []
            if len(n) == 1:
                r.append(n)
            elif n[0] == '0':
                if n[-1] != '0':
                    r.append(n[0] + '.' + n[1:])
            else:
                if n[-1] == '0':
                    r.append(n)
                else:
                    for i in range(len(n) - 1):
                        r.append(n[:i+1] + '.' + n[i+1:])
            return fun
        for i in range(len(s1) - 1):
            n1 = s1[:i+1]
            n2 = s1[i+1:]
            for nn1 in fun(n1):
                for nn2 in fun(n2):
                    ans.append("("+nn1+", "+nn2+")")
        return ans