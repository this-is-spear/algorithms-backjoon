import sys

i = int(input())
arr = list(map(int, input().split()))
arr.sort()

if arr[0] != 1:
    print(1)
else:
    sum_int = arr[0]
    for i in range(1, i):
        if arr[i] > sum_int + 1:
            print(sum_int+1)
            sys.exit(0)
        sum_int += arr[i]
    print(sum_int+1)
