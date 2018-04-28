class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st = path.split('/')
        s = set(['.','..',''])
        l = []
        for name in st:
            if name not in s:
                l.append(name)
            elif name == '..':
                if len(l) > 0:
                    l.pop()
        res = ''
        while len(l) > 0:
            res = '/'+l.pop()+res
        if res == '':
            res = '/'
        return res