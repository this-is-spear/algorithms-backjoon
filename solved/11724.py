from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
rc = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    rc[a-1][b-1] = 1
    rc[b-1][a-1] = 1
answer = 0
visited_num = set()
deque = deque([])
for i in range(n):
    if i not in visited_num:
        answer += 1
        visited_num.add(i)
        deque.append(i)
        while deque:
            item = deque.popleft()
            for k in range(len(rc)):
                if rc[item][k] == 1 and k not in visited_num:
                    deque.append(k)
                    visited_num.add(k)
print(answer)