nn = int(input())
for __ in range(nn):
    a = list(map(int, input().split(' ')))
    n = a[0]
    del a[0]
    m = a[0]
    del a[0]
    i = 0
    now = 0
    b = [i for i in range(n)]
    for j in range(n-1):
        now = (now  + a[i] - 1) % (n - j)
        del b[now]
        if now == n - j:
            now = 0
        i = (i + 1) % m
    print(b[0])
