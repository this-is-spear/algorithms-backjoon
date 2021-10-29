from collections import deque
from sys import stdin
input = stdin.readline
a, b = int(input()), int(input())
arr = [[0] * a for _ in range(a)]
visited = [[0] * a for _ in range(a)]
for _ in range(b):
    i, k = map(int, input().split())
    arr[i - 1][k - 1] = 1
    arr[k - 1][i - 1] = 1

deque = deque([])
visited = [0]
for k_len in range(len(arr[0])):
    if arr[0][k_len] == 1:
        deque.append([0, k_len])
        visited.append(k_len)
answer = 0
while deque:
    answer += 1
    a, b = deque.popleft()
    for i in range(len(arr[0])):
        if arr[b][i] == 1:
            if i not in visited:
                deque.append([b, i])
                visited.append(i)
print(answer)
