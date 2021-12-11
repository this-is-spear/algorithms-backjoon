arr1 = [500] * 1 + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 + [10] * 6
arr2 = [512] * 1 + [256] * 2 + [128] * 4 + [64] * 8 + [32] * 16
for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = 0
    if 0 < a < 22:
        answer += arr1[a - 1]
    if 0 < b < 32:
        answer += arr2[b - 1]
    print(answer * 10000)
