import copy
from collections import deque
for _ in range(int(input())):
    _, index = map(int, input().split())
    a = list(map(int, input().split()))
    arr = []
    q = deque([])
    temp = 0
    for i, k in enumerate(a):
        q.append([i,k])
    while q:
        q_pop = q.popleft()
        if q:
            for k in copy.deepcopy(q):
                if q_pop[1] < k[1]:
                    q.append(q_pop)
                    break
            else:
                temp += 1
                if index == q_pop[0]:
                    print(temp)
                    break
        else:
            temp += 1
            print(temp)
