class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d = {}
        se = set(banned)
        se.add("")
        s = paragraph.lower()
        for i in range(len(s)):
            if not s[i].isalpha() and s[i] != ' ':
                s = s.replace(s[i], ' ')
        while '  ' in s:
            s = s.replace('  ', ' ')
        s.strip()
        l = s.split(' ')
        print(s)
        best = 0
        ans = ""
        for i, x in enumerate(l):
            if x not in se:
                if x not in d:
                    d[x] = 1
                else:
                    d[x] += 1
                if best < d[x]:
                    best = d[x]
                    ans = x
        return ans
