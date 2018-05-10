class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        q = []
        ans = 0
        for i in range(int(math.sqrt(N))):
            if N % i == 0:
                q.append([i, N//i])
        for p in q:
            x = p[0]
            y = p[1]
            if x % 2 == 1:
                ans += 1
            if y != x and y % 2 == 1:
                if x - y // 2 > 0:
                    ans += 1
            if x % 2 == 1 and y % 2 == 1 and x >= y // 2:
                ans += 1
        return ans