def sol(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return sol(a - 1) + sol(a - 2)

import sys
i = int(sys.stdin.readline())
print(sol(i))
