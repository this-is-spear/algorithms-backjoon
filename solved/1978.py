# 1000이하의 소수를 먼저 찾자
input()
arr2 = map(int, input().split())
answer = 0
arr = {i for i in range(2, 1001)}
for i in range(2, int(1000 ** 0.5) + 1):
    for k in range(2 * i, 1001, i):
        arr -= {k}
print(len([i for i in arr2 if i in arr]))
