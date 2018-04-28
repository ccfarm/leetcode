class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        height = [[0 for y in range(n)]for m in range(m)]
        ans = 0
        for i in range(m):
            stack = []
            for j in range(n):
                if i > 0:
                    if matrix[i][j] == '1':
                        height[i][j] = height[i-1][j] + 1
                    else:
                        height[i][j] = 0
                else:
                    if matrix[i][j] == '1':
                        height[i][j] = 1
                    else:
                        height[i][j] = 0
                if stack == [] or height[i][j] > height[i][stack[-1]]:
                    stack.append(j)
                else:
                    while stack != [] and height[i][j] <= height[i][stack[-1]]:
                        x = height[i][stack.pop()]
                        if stack == []:
                            l = -1
                        else:
                            l = stack[-1]
                        #print(i, j, l, x)
                        ans = max(ans, x * (j - l - 1));
                    stack.append(j)
            while stack != []:
                x = height[i][stack.pop()]
                if stack == []:
                    l = -1
                else:
                    l = stack[-1]
                #print(i, j, l, x)
                ans = max(ans, x * (n - l - 1));
        #print(height)
        return ans