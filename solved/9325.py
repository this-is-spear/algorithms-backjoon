import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = int(input())
    for _ in range(int(input())):
        b,c = map(int,input().split())
        a += b*c
    print(a)