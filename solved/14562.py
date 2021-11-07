from collections import deque

for _ in range(int(input())):
    a, b = map(int, input().split())
    que = deque([[(a, b), 0]])
    while True:
        q_item = que.popleft()
        if q_item[0][0] == q_item[0][1]:
            print(q_item[1])
            break
        if 2 * q_item[0][0] <= q_item[0][1]  + 3:
            que.append([(2*q_item[0][0],q_item[0][1]+3), q_item[1]+1])

        if q_item[0][0] <= q_item[0][1]:
            que.append([(q_item[0][0]+1,q_item[0][1]), q_item[1]+1])