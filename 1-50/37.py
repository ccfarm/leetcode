class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set([]) for _ in range(9)]
        colum = [set([]) for _ in range(9)]
        block = [[set([]) for y in range(3)]for x in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    colum[j].add(board[i][j])
                    block[i // 3][j // 3].add(board[i][j])
        def dfs(n):
            if n == 81:
                return True
            i = n // 9
            j = n % 9
            if board[i][j] != '.':
                return dfs(n + 1)
            else:
                for x in range(1, 10):
                    s = str(x)
                    if s not in row[i] and s not in colum[j] and s not in block[i // 3][j // 3]:
                        board[i][j] = s
                        row[i].add(s)
                        colum[j].add(s)
                        block[i // 3][j // 3].add(s)
                        if dfs(n + 1):
                            return True
                        row[i].remove(s)
                        colum[j].remove(s)
                        block[i // 3][j // 3].remove(s)
                        board[i][j] = '.'
        dfs(0)
