import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop()
    arr.pop()
    print(arr.pop())
