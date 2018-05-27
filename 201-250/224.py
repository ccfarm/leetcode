class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = []
        s2 = []
        sigh1 = set['+', '-']
        i = 0
        l = len(s)
        while i < l:
            if s[i] >= '0' and s[i] <= '9':
                tmp = 0
                while s[i] >= '0' and s[i] <= '9':
                    tmp = tmp * 10 + ord(s[i]) - ord('0')
                    i += 1
                s1.append(tmp)
            elif s[i] in sigh1:
                if s2 != [] and s2[-1] in sigh1:
                    ch = s2.pop()
                    b = s1.pop()
                    a = s1.pop()
                    if ch == '+':
                        s1.append(a + b)
                    elif ch == '-':
                        s1.append(a-b)
                s2.append(s[i])
                i += 1
            elif s[i] == '(':
                s2.append(s[i])
                i += 1
            else:
                if s2 != [] and s2[-1] in sigh1:
                    ch = s2.pop()
                    b = s1.pop()
                    a = s1.pop()
                    if ch == '+':
                        s1.append(a + b)
                    elif ch == '-':
                        s1.append(a-b)
                s2.pop()
                i += 1
        if s2 != [] and s2[-1] in sigh1:
            ch = s2.pop()
            b = s1.pop()
            a = s1.pop()
            if ch == '+':
                s1.append(a + b)
            elif ch == '-':
                s1.append(a - b)
        return s1[0]
