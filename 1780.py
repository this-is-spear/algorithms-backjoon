import sys
input = sys.stdin.readline

a = int(input())
answer = [0, 0, 0]
# 배열 생성
arr = []
for _ in range(a):
    temp = list(map(int, input().split()))
    arr.append(temp)
visited = [[0] * a for _ in range(a)]
temp = a
# 부분 체크
def checkVisited(i, k, temp):
    for temp_i in range(i, i + temp):
        for temp_k in range(k, k + temp):
            visited[temp_i][temp_k] = 1

# 전체 확인
while temp > 0:
    for i in range(0, a, temp):
        for k in range(0, a, temp):
            if visited[i][k] != 1:
                plus_count = 0
                minus_count = 0
                zero_count = 0
                for t in range(0, temp):
                    if arr[k + t][i:i + temp].count(1) == temp:
                        plus_count += 1
                    elif arr[k + t][i:i + temp].count(0) == temp:
                        zero_count += 1
                    elif arr[k + t][i:i + temp].count(-1) == temp:
                        minus_count += 1
                if plus_count == temp:
                    answer[2] += 1
                    checkVisited(i, k, temp)
                elif minus_count == temp:
                    answer[0] += 1
                    checkVisited(i, k, temp)
                elif zero_count == temp:
                    answer[1] += 1
                    checkVisited(i, k, temp)
    temp = temp // 3
print('\n'.join(str(i) for i in answer))
