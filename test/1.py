line = input().split(' ')
n = int(line[0])
m = int(line[1])
a = []
d = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }
d1 = {}
li = [16**i for i in range(7)]
for _ in range(n):
    line = input().split(' ')
    a.append([])
    for x in line:
        if x not in d1:
            tmp = 0
            j = len(x) - 1
            while j >= 0:
                tmp = tmp * 16 + d[x[j]]
                j -= 1
            i = 0
            while tmp > 0:
                if tmp % 2 == 0:
                    i += 1
                    tmp //= 2
                else:
                    break
            a[_].append(i)
            d1[x] = i
        else:
            a[_].append(d1[x])
dp = [[0 for y in range(m)] for x in range(n)]
ro = [['' for y in range(m)] for x in range(n)]
dp[0][0] = a[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + a[i][0]
    ro[i][0] = 'V'
for j in range(1,m):
    dp[0][j] = dp[0][j-1] + a[i][j]
    ro[0][j] = '>'
for i in range(1, n):
    for j in range(1, m):
        tmp = 0
        if dp[i-1][j] <= dp[i][j-1]:
            tmp = dp[i-1][j]
            ro[i][j] = 'V'
        else:
            tmp = dp[i][j-1]
            ro[i][j] = '>'
        dp[i][j] = tmp + a[i][j]

print(dp[n-1][m-1] // 4)
i = n-1
j = m-1
st = ''
while i > 0 or j > 0:
    st = ro[i][j] + st
    print(st)
    if ro[i][j] == 'V':
        i -= 1
    else:
        j -= 1
print(st)
best = dp[n-1][m-1]
