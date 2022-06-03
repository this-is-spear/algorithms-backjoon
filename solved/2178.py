# 데크를 사용해서 문제를 해결할 수 있어보인다.
# 입력 값은 2이상 100이하이다.
# 1. 현재보다 큰 숫자가 적인 칸이거나 숫자가 1인 칸인지 확인한다.
# 2. 맞다면 해당 칸에 이동한다.
# 3. 자신이 들고 있는 값으로 해당 칸을 갱신한다.
# 4. 1번부터 3번을 반복한다.
# 5. N*M 칸에 적힌 숫자를 반환한다.

from collections import deque

a, b = map(int, input().split())
arr = [list(i for i in map(int, input())) for _ in range(a)]

de = deque()
de.append([0, 0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while de:
    item = de.popleft()
    for i in range(4):
        x = item[0] + dx[i]
        y = item[1] + dy[i]
        if a > x >= 0 and b > y >= 0 and not (x == 0 and y == 0):
            if arr[x][y] != 0:
                if arr[x][y] == 1 or arr[item[0]][item[1]] + 1 < arr[x][y]:
                    de.append([x, y])
                    arr[x][y] += arr[item[0]][item[1]]

print(arr[a-1][b-1])
