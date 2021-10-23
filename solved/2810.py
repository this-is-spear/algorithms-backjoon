import sys

input = sys.stdin.readline
c, a = int(input()), input()
print(c if len(a) - a.count("L") // 2 > c else len(a) - a.count("L") // 2)
