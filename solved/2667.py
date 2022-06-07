# 1. 집을 조사했는지 여부를 가지는 배열을 준비한다.
# 2. 단지의 개수를 모을 배열을 준비한다.
# 3. 조사하지 않은 집을 조사한다.
# 4. 1이 나오면 값이 1인 count를 생성하고, 주변 상하좌우 집을 조사한다.
# 5. 집이 있으면 집 조사 여부 배열에 체크를 하고, count를 1 증가시킨다.
# 6. 집이 없을 때까지 확인한다.
# 7. 더 이상 집이 없으면 다음 집을 찾아 떠난다.
# 8. 3번 부터 7번까지 반복한다.

from collections import deque
import heapq

a = int(input())

arr = []
temp_arr = []
result = []
#     상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def print_result():
    global result
    print(len(result))
    while result:
        print(heapq.heappop(result))


for _ in range(a):
    input_str = input()
    arr.append([i for i in input_str])
    temp_arr.append([False if i == '0' else True for i in input_str])

for i in range(a ** 2):
    if temp_arr[i // a][i % a] and arr[i // a][i % a] == '1':
        de = deque([[i // a, i % a]])
        temp_arr[i // a][i % a] = False
        count = 1
        while de:
            item = de.popleft()
            for index in range(4):
                index_y = item[0] + dy[index]
                index_x = item[1] + dx[index]
                if a > index_y >= 0 and a > index_x >= 0:
                    if temp_arr[index_y][index_x] and arr[i // a][i % a] == '1':
                        temp_arr[index_y][index_x] = False
                        de.append([index_y, index_x])
                        count += 1
        else:
            heapq.heappush(result, count)
print_result()
