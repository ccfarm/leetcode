class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(10):
            if not self.isValid(self, i, i, 0, 8):
                return False
            if not self.ifValid(self, 0, 8, i, i):
                return False
        for i in range(3):
            for j in range(3):
                if not self.ifValid(self, i * 3, i * 3 + 2, j * 3, j * 3 + 2):
                    return False
        return True
    def isValid(self, board, i1, i2, j1, j2):
        s = set([])
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        return True