# 제일 작은 거리의 최대값을 구하라


a, b = map(int, input().split())
arr = sorted([int(input()) for _ in range(a)])

arr.sort()
rt = 1
lt = arr[-1] - arr[0]
answer = 0

while rt <= lt:
    mid = (rt + lt)//2
    old = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= old+mid:
            count += 1
            old = arr[i]

    if count >= b:
        rt = mid + 1
        answer = mid
    else:
        lt = mid - 1

print(answer)