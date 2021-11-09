import sys
arr = [0]*10001
for _ in range(int(input())):
    arr[int(sys.stdin.readline())] += 1

for k, i in enumerate(arr):
    if i != 0:
        for i in range(i):
            sys.stdout.write(str(k) + '\n')
