class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(0, n-2):
            for j in range(0, m-2):
                s = set()
                flag = 0
                for ii in range(3):
                    for jj in range(3):
                        if grid[i+ii] not in s:
                            s.add(grid[i+ii][j+jj])
                        else:
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 1:
                    continue
                for ii in range(3):
                    t1 = 0
                    t2 = 0
                    for jj in range(3):
                        t1 += grid[i+ii][j+jj]
                        t2 += grid[j+jj][i+ii]
                    if t1 != 15 or t2 != 15:
                        flag = 1
                        break
                if flag == 1:
                    continue
                t3 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                t4 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                if t1 != 15 or t2 != 15:
                    continue
                ans += 1
        return ans

