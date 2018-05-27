class Solution:
    def do(self, n,m,a):
        sum = [0]
        for i in range(n):
            sum.append(sum[-1] + a[i])
        self.t = sum[n] / m
        self.ans = sum[n]
        def f(d, now, maxx):
            if d >= n:
                return
            elif now == m:
                tmp = max(maxx, sum[n] - sum[d])
                self.ans = min(self.ans, tmp)
            else:
                tt = self.t * now
                i = d
                while i < n and sum[i] < tt:
                    i += 1
                if i > d and sum[i] > tt:
                    f(i-1, now+1, maxx)
                f(i, now+1, max(maxx, sum[i] - sum[d]))
        f(0, 1, 0)
        return self.ans


if __name__ == "__main__":


    line = input().split(' ')
    n = int(line[0])
    m = int(line[1])
    line = input().split()
    a = list(map(int, line))
    s = Solution()
    print(s.do(n,m,a))