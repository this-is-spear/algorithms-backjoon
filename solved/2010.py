import sys
input = sys.stdin.readline
answer = 0
for _ in range(int(input())):
    a = int(input())
    if answer != 0:
        answer += a - 1
    else:
        answer += a
print(answer)