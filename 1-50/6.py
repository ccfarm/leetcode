class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[] for x in range(numRows)]
        i = 0
        l = len(s)
        n = numRows
        if n == 1:
            return s
        while i < l:
            for j in range(n - 1):
                if i >= l:
                    break
                arr[j].append(s[i])
                i += 1
            for j in reversed(range(1, n)):
                if i >= l:
                    break
                arr[j].append(s[i])
                i += 1
        strs = [''.join(arr[x]) for x in range(n)]
        return ''.join(strs)

s = Solution()
print(s.convert("A", 1))
