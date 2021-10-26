# import sys
# sys.setrecursionlimit(10**6)
# arr = []
# for i in range(int(input())):
#     arr.append(list(map(int, input().split())))
# an = 0
# def sol(a, b):
#     global an
#     if arr[a][b] == -1:
#         an = 1
#         return
#     if b + arr[a][b] < len(arr):
#         sol(a, b + arr[a][b])
#     if a+arr[a][b] < len(arr):
#         sol(a + arr[a][b], b)
# # a,b = 0,0
# # while  b + arr[a][b]
# # < len(arr) or a+arr[a][b] < len(arr):
# #     if arr[a][b] == -1:
# #         break
# #     if b + arr[a][b] < len(arr):
# #         b = b + arr[a][b]
# #     if a+arr[a][b] < len(arr):
# #         a = a+ arr[a][b]
# sol(0,0)
# if an == 1:
#     print("HaruHaru")
# else:
#     print("Hing")

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1]
dy = [1, 0]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
flag = False
queue = deque([[0,0]])
visited = [[False]*N for _ in range(N)]

while queue:
    x,y = queue.popleft()
    if arr[x][y] == 0:
        break
    if arr[x][y] == -1:
        flag = True
        break
    for i in range(2):
        nx = x+arr[x][y]*dx[i]
        ny = y+arr[x][y]*dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            queue.append([nx, ny])
            visited[nx][ny] = True

if flag:
    print("HaruHaru")
else:
    print("Hing")
