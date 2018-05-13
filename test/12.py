def f(s1,s2):
    l = len(s1)
    if len(s2) < l:
        return False
    i = 0
    while i < l and s1[i] == s2[i]:
        i += 1
    if i == l:
        return True
    else:
        return False

flag = 0
while True:
    try:
        line = input()
        if line.strip() == '':
            continue
    except:
        break



    line = line.split(' ')
    line = map(int, line)
    line = list(line)
    n = line[0]
    m = line[1]
    d = []
    for i in range(n):
        d.append(input())

    input()

    if flag:
        print()
    else:
        flag = 1

    for i in range(m):
        tmp = input()
        for j in range(n):
            if f(d[j], tmp):
                print(1)
                break
        else:
            print(-1)
