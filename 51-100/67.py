class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = ""
        i = len(a) - 1
        j = len(b) - 1
        flag = 0
        while i >= 0 or j >= 0:
            count = flag
            if i >= 0 and a[i] == 1:
                count += 1
            if j >= 0 and b[j] == 1:
                count += 1
            c = str(count % 2) + c
            flag = count // 2
        if flag == 1:
            c = "1" + c
        return c