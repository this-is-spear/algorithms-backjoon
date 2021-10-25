def sol(a,b):
    while a:
        a_pop = a.pop(0)
        if b.count(a_pop):
            b = b[b.index(a_pop)+1:]
        else:
            print('No')
            break
    else:
        print('Yes')


import sys
input = sys.stdin.readline
while True:
    line = input().strip()
    if not line:
        break

    s,t = map(list, line.split())
    sol(s, t)
