from collections import deque
n = int(input())
a = deque(i for i in range(1, n+1))
while a:
    k = a.popleft()
    if a:
        a.append(a.popleft())
    else:
        print(k)