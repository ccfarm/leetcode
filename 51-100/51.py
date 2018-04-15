class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for y in range(n)]for x in range(n)]
        col = [True for i in range(n)]
        s1 = [True for i in range(2 * n - 1)]
        s2 = [True for i in range(2 * n - 1)]
        ans = []
        def dfs(i):
            if i >= n:
                ans1 = []
                for row in board:
                    st = ''.join(row)
                    ans1.append(st)
                ans.append(ans1)
            else:
                for j in range(n):
                    if col[j] and s1[i + j] and s2[i - j + n - 1]:
                        board[i][j] = 'Q'
                        col[j] = False
                        s1[i + j] = False
                        s2[i - j + n - 1] = False
                        dfs(i + 1)
                        board[i][j] = '.'
                        col[j] = True
                        s1[i + j] = True
                        s2[i - j + n - 1] = True
        dfs(0)
        return ans