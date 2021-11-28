import sys
input = sys.stdin.readline
for _ in range(3):
    answer = 0
    for _ in range(int(input())):
        answer += int(input())
    else:
        if answer > 0:
            print("+")
        elif answer < 0:
            print("-")
        else:
            print(0)
