#
# a ,b = map(int, input().split())
# arr = {}
# for _ in range(a):
#     arr.setdefault(input(), 0)
#
# for _ in range(b):
#     k = input()
#     if k in arr:
#         arr[k] += 1
#
# print(sum(arr.values()))
# for i in sorted(arr.items()):
#     if i[1] == 1:
#         print(i[0])
#
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)