n = int(input())
a = []
for i in range(n):
    line = input().split(' ')
    line = list(map(int, line))
    a.append(line)
a.sort(key=lambda x: x[1], reverse=True)
top = 0
for i,x in enumerate(a):
    if x[0] > top:
        print(x[0], x[1])