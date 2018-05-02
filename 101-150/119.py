class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex):
            tmp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(tmp.copy())
        return ans[rowIndex-1]