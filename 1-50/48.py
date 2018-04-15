class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def trans(x, y):
            x, y = y, n - 1 - x
            return x, y
        s = set([])
        for i in range(n // 2 + 1):
            for j in range(n // 2 + 1):
                    x1, y1 = i, j
                    x2, y2 = trans(x1, y1)
                    x3, y3 = trans(x2, y2)
                    x4, y4 = trans(x3, y3)
                    if (x1, y1) not in s:
                        s.add(x1,y1)
                        s.add(x2, y2)
                        s.add(x3, y3)
                        s.add(x4, y4)
                        matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = \
                            matrix[x4][y4], matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]
