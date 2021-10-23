import sys

input = sys.stdin.readline
_, b, c = int(input()), list(map(int, input().split())), list(map(int, input().split()))
temp = c[0]
an = 0
for i in c[:-1]:
    b_pop = b.pop(0)
    if i < temp:
        temp = i
    an += temp * b_pop
print(an)
