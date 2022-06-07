# 순서대로 인덱스를 검사해 섬을 찾는다.
# 상하좌우 그리고 대각선으로 연결되면 같은 지역의 섬이다.
# 0이 두개 주어지면 종료한다.

from collections import deque

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    arr = []
    temp_arr = []
    result = 0

    dx = [-1, 0, 1, -1, 0, 1, -1, 1]
    dy = [1, 1, 1, -1, -1, -1, 0, 0]

    for _ in range(b):
        input_list = input().split()
        arr.append(input_list)
        temp_arr.append([True if i == '1' else False for i in input_list])

    for i in range(a * b):
        if temp_arr[i // a][i % a] and arr[i // a][i % a] == '1':
            de = deque([[i // a, i % a]])
            temp_arr[i // a][i % a] = False
            result += 1
            while de:
                item = de.popleft()
                for index in range(8):
                    index_dx = item[1] + dx[index]
                    index_dy = item[0] + dy[index]
                    if a > index_dx >= 0 and b > index_dy >= 0:
                        if temp_arr[index_dy][index_dx] and arr[index_dy][index_dx] == '1':
                            de.append([index_dy, index_dx])
                            temp_arr[index_dy][index_dx] = False
    print(result)
