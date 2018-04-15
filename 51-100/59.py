class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for x in range(n)]for y in range(n)]
        i = 0
        count = 1
        nn = n
        while nn >= 2:
            for j in range(nn - 1):
                ans[i][i + j] = count
                count += 1
            for j in range(nn - 1):
                ans[i + j][i + nn - 1] = count
                count += 1
            for j in range(nn - 1):
                ans[i + nn - 1][i + nn - 1 - j] = count
                count += 1
            for j in range(nn - 1):
                ans[i + nn - 1 - j][i] = count
                count += 1
            i += 1
            nn -= 2
        if nn == 1:
            ans[i][i] = count
        return ans