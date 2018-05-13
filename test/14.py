s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)
i = 0
j = 0
ans = 100
pre = -1
while i < l1:
    while j < l2 and s1[i] != s2[j]:
        j += 1
    if j < l2:
        if pre != -1:
            ans -= (j - pre - 1)
        pre = j
        j += 1
        i += 1
    else:
        break
if j < l2:
    print(ans)
else:
    print(0)
