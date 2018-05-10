class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S.find('@') != -1:
            S = S.lower()
            l = S.split('@')
            ll = len(l[0])
            l[0] = l[0][0] + '*' * 5 + l[0][-1]
            return '@'.join(l)
        else:
            l = []
            for i in range(S):
                if S[i].isdigit():
                    l.append(S[i])
            ll = len(l)
            s1 = '***-***-' + ''.join(l[-4:])
            if l > 10:
                s2 = '+' + ''.join(l[:-10]) + '-'
            return s2 + s1