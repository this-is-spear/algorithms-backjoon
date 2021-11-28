import sys
from collections import deque

input = sys.stdin.readline
a, b, c = 0, 0, 0


def findOne(k, i):
    visited[k][i] = 1
    de = deque([[k, i]])
    while de:
        k, i = de.popleft()
        # 오른쪽 아래일 경우 에러
        if a-1 > k:
            if arr[k + 1][i] == 1 and visited[k + 1][i] != 1:
                de.append([k + 1, i])
                visited[k + 1][i] = 1
        if b-1 > i:
            if arr[k][i + 1] == 1 and visited[k][i + 1] != 1:
                de.append([k, i + 1])
                visited[k][i + 1] = 1
            # 왼쪽 위일 경우 에러
        if k > 0:
            if arr[k - 1][i] == 1 and visited[k - 1][i] != 1:
                de.append([k - 1, i])
                visited[k - 1][i] = 1
        if i > 0:
            if arr[k][i - 1] == 1 and visited[k][i - 1] != 1:
                de.append([k, i - 1])
                visited[k][i - 1] = 1

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    arr = [[0] * b for _ in range(a)]
    visited = [[0] * b for _ in range(a)]
    answer = 0
    for _ in range(c):
        i, k = map(int, input().split())
        arr[i][k] = 1
    for i in range(a * b):
        if arr[i // b][i % b] == 1 and visited[i // b][i % b] != 1:
            findOne(i // b, i % b)
            answer += 1
    print(answer)
