#coding=utf-8
import sys
flag1 = True
flag2 = False
ans = 0
for line in sys.stdin:
    l = len(line)
    i = 0
    this = 0
    if flag2:
        this = 1
    while i < l:
        if line[i] == '"':
            flag1 = not flag1
            i += 1
        elif line[i] == '/':
            i += 1
            if i< l and line[i] == '/':
                i += 1
                if flag1:
                    this = 1
            if i < l and line[i] == '*':
                i += 1
                if flag1:
                    this = 1
                    flag2 = True
        elif line[i] == '*':
            i += 1
            if i< l and line[i] == '/':
                i += 1
                flag2 = False
        ans += this
    print(ans)