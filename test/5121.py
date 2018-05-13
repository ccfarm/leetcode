n = int(input())
a = list(map(int, input().split(' ')))
line = input().split(' ')
p = int(line[0])
s = int(line[1])
p = s // p
a.sort(reverse=True)

a.append(0)
ans = a[0]
times = 0
now = 0
while p > 0:
    if a[now] == 0:
        ans = 0
        break
    while a[now] == a[now+1]:
        now += 1
    gap = a[now] - a[now+1]
    if p >= gap * (now + 1):
        p -= gap * (now + 1)
        ans = a[now + 1]
        now += 1
    else:
        p = 0
        ans = a[now] - p // (now + 1)
print(ans)