class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        a = [[1 for j in range(m)] for i in range(n)]
        def dfs(i,j):
            a[i,j] = 0
            if i > 0 and a[i-1][j] == 1:
                dfs(i-1, j)
            if i+1 < n and a[i+1][j] == 1:
                dfs(i+1, j)
            if j > 0 and a[i][j-1] == 1:
                dfs(i, j-1)
            if j+1 < m and a[i][j+1] == 1:
                dfs(i, j+1)
        ans = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    ans += 1
                    dfs(i, j)
        return ans
