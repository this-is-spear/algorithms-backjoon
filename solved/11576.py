import sys
input = sys.stdin.readline
a, b = map(int,input().split())
c = int(input())
d = list(map(int,input().split()))
answer = 0
for k in range(c):
    answer += d[k]*a**(c-k-1)

temp = []
while answer > 0:
    temp.append(answer%b)
    answer = answer//b

for k in range(len(temp)-1, -1, -1):
    print(temp[k], end=' ')

