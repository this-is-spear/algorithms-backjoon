import sys

input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == 0:
        sys.exit(0)
    else:
        print('Yes' if a > b else 'No')
