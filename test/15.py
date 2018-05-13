class solution:
    def __init__(self, n,m,a):
        self.n = n
        self.m = m
        self.a = a
        self.ans = 0

    def f(self):
        def dfs(i,j,now,flag):
            if j >= self.m:
                return
            if flag == 0 and a[i][j] + now < 0:
                return
            now = now + a[i][j]
            self.ans = max(self.ans, now,flag)
            if i > 0:
                dfs(i-1, j+1,now,flag)
            dfs(i, j+1, now, flag)
            if i+1 < self.n:
                dfs(i+1, j+1, now,flag)

            if a[i][j] < 0 and flag == 1:
                now = now - 2 * a[i][j]
                self.ans = max(self.ans, now, 0)
                if i > 0:
                    dfs(i - 1, j + 1, now, 0)
                dfs(i, j + 1, now, 0)
                if i + 1 < self.n:
                    dfs(i + 1, j + 1, now, 0)


        for i in range(n):
            dfs(i,0,0,1)
        return self.ans


line = input().split(' ')
line = list(map(int, line))
n = line[0]
m = line[1]
a = []
for i in range(n):
    line = input().split(' ')
    line = list(map(int, line))
    a.append(line)

print(solution(n,m,a).f())