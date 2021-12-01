import sys
from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
deque = deque([[n, 0]])
while deque:
    item = deque.popleft()
    if item[0] <= 100000:
        if visited[item[0]] == 0:
            if item[0] == k:
                print(item[1])
                sys.exit(0)
            if item[0] > k:
                deque.append([item[0] - 1, item[1] + 1])
            else:
                if item[0]+1 <=100000:
                    deque.append([item[0] + 1, item[1] + 1])
                if item[0]>0:
                    deque.append([item[0] - 1, item[1] + 1])
                if item[0]*2 <= 100000:
                    deque.append([item[0] * 2, item[1] + 1])
            visited[item[0]] = 1
