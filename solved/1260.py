a, b, c = map(int, input().split())
arr = [[0] * a for _ in range(a)]
for _ in range(b):
    i, k = map(int, input().split())
    arr[i - 1][k - 1] = 1
    arr[k - 1][i - 1] = 1

# DFS
visited = [0] * a
visited[c - 1] = 1
dfs_arr = []


def dfs(i):
    dfs_arr.append(i + 1)
    visited[i] = 1
    for k in range(a):
        if arr[i][k] == 1 and visited[k] == 0:
            dfs(k)


dfs(c - 1)
print(' '.join(str(i) for i in dfs_arr))

# BFS
from collections import deque

deque = deque([c - 1])
bfs_arr = [c]
visited = [0] * a
visited[c - 1] = 1

while deque:
    item = deque.popleft()
    for i in range(len(arr[item])):
        if arr[item][i] == 1 and visited[i] == 0:
            deque.append(i)
            bfs_arr.append(i + 1)
            visited[i] = 1

print(' '.join(str(i) for i in bfs_arr))
