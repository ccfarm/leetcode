class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        a = [[0.0 for y in range(x + 1)]for x in range(101)]
        a[0][0] = poured
        for i in range(100):
            for j in range(i + 1):
                if a[i][j] > 1:
                    p = a[i][j] - 1.0
                    a[i][j] = 1.0
                    a[i + 1][j] += p / 2
                    a[i + 1][j + 1] += p / 2

        return a[query_row][query_glass]