import sys

arr = []
for _ in range(5):
    arr += list(map(int, input().split()))


def sol(arr):
    anwer = 0
    for i in range(5):
        if sum(arr[i * 5 + 0:i * 5 + 5]) == 0:
            anwer += 1
        if sum(arr[0 + i:25:5]) == 0:
            anwer += 1
    if sum(arr[0:25:6]) == 0:
        anwer += 1
    if sum(arr[4:24:4]) == 0:
        anwer += 1
    return anwer


for k in range(5):
    temp = map(int, input().split())
    for enum, i in enumerate(temp):
        if i in arr:
            arr[arr.index(i)] = 0
            if sol(arr) >= 3:
                print(k * 5 + enum + 1)
                sys.exit(0)
