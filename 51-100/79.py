class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        l = len(word)
        if l == 0:
            return True
        def dfs(i,j,k):
            if k >= l:
                return True
            if i > 0 and board[i-1][j] == word[k]:
                temp = board[i-1][j]
                board[i-1][j] = '*'
                if dfs(i-1,j,k+1):
                    return True
                board[i-1][j] = temp
            if j > 0 and board[i][j-1] == word[k]:
                temp = board[i][j-1]
                board[i][j-1] = '*'
                if dfs(i,j-1,k+1):
                    return True
                board[i][j-1] = temp
            if i < m-1 and board[i+1][j] == word[k]:
                temp = board[i+1][j]
                board[i+1][j] = '*'
                if dfs(i+1,j,k+1):
                    return True
                board[i+1][j] = temp
            if j < n-1 and board[i][j+1] == word[k]:
                temp = board[i][j+1]
                board[i][j+1] = '*'
                if dfs(i,j+1,k+1):
                    return True
                board[i][j+1] = temp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = '*'
                    if dfs(i,j,1):
                        return True
                    board[i][j] = temp
        return False