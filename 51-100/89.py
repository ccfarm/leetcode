class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        ans = [0, 1]
        k = 1
        for i in range(2, n+1):
            k *= 2
            temp = ans.copy()
            for j in reversed(range(len(ans))):
                temp.append(ans[j] + k)
            ans = temp.copy()
        return ans
