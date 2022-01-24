import sys
a, b = map(int, input().split())
arr = [True] * (a+1)
answer = 0
for i in range(2, len(arr)+1):
    for k in range(i, a+1, i):
        if arr[k]:
            arr[k] = False
            answer += 1
            if answer == b:
                print(k)
                sys.exit(0)

