class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        s = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in s:
                    s.add(i, j)
                    if board[i][j] == 'O':
                        flag = 1
                        q = [i,j]
                        q1 = [i,j]
                        while q1:
                            ii, jj = q1.pop()
                            if ii == 0 or ii == m-1 or jj == 0 or jj == n-1:
                                flag = 0
                            if ii > 0 and (ii-1,jj) not in s and board[ii-1][jj] == 'O':
                                s.add(ii-1, jj)
                                q1.append(ii-1,jj)
                                q.append(ii-1,jj)
                            if ii < m-1 and (ii+1,jj) not in s and board[ii+1][jj] == 'O':
                                s.add(ii+1, jj)
                                q1.append(ii+1,jj)
                                q.append(ii+1,jj)
                            if jj > 0 and (ii,jj-1) not in s and board[ii][jj-1] == 'O':
                                s.add(ii, jj-1)
                                q1.append(ii,jj-1)
                                q.append(ii,jj-1)
                            if jj < n-1 and (ii,jj+1) not in s and board[ii][jj+1] == 'O':
                                s.add(ii, jj+1)
                                q1.append(ii,jj+1)
                                q.append(ii,jj+1)
                        if flag == 1:
                            while q:
                                ii, jj = q.pop()
                                board[ii][jj] = 'X'