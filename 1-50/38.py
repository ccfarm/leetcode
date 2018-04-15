class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        i = 1
        while i < n:
            st = ""
            count = 1
            now = s[0]
            for j in range(1, len(s)):
                if s[j] == now:
                    count += 1
                else:
                    st = st + str(count) + now
                    count = 1
                    now = s[j]
            st = st + str(count) + now
            s = st
            i += 1
            print(s)
        return s