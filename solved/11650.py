# arr = []
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     arr.append((a, b))
# print('\n'.join(str(i[0]) + ' ' + str(i[1]) for i in sorted(arr, key=lambda x: (x[0], x[1]))))

import sys

N = int(input())

li = [sys.stdin.readline() for _ in range(N)]
li.sort(key=lambda x: tuple(map(int, x.split())))

print(''.join(li))
