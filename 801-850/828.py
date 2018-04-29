class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        map = [[-1]*n for _ in range(m)]
        self.count = 0
        z = []
        def dfs(i, j):
            map[i][j] = self.count
            z[self.count-1] += 1
            if i>0 and grid[i-1][j] == 1 and map[i-1][j] == -1:
                dfs(i-1, j)
            if j>0 and grid[i][j-1] == 1 and map[i][j-1] == -1:
                dfs(i, j-1)
            if i<m-1 and grid[i+1][j] == 1 and map[i+1][j] == -1:
                dfs(i+1,j)
            if j<n-1 and grid[i][j+1] == 1 and map[i][j+1] == -1:
                dfs(i,j+1)
        for i in range(m):
            for j in range(n):
                if map[i][j] == -1:
                    if grid[i][j] == 0:
                        map[i][j] = 0
                    else:
                        self.count += 1
                        z.append(0)
                        dfs(i, j)
        ans = 0
        for i in range(self.count):
            ans = max(ans, z[i])
        if ans < m * n:
            ans += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    l = set([])
                    if i > 0 and map[i-1][j] != 0:
                        l.add(map[i-1][j])
                    if j > 0 and map[i][j-1] != 0:
                        l.add(map[i][j-1])
                    if i < m-1 and map[i+1][j] != 0:
                        l.add(map[i+1][j])
                    if j < n-1 and map[i][j+1] != 0:
                        l.add(map[i][j+1])
                    for x in l:
                        for y in l:
                            if x != y:
                                ans = max(ans, z[x-1] + z[y-1] + 1)
        return ans