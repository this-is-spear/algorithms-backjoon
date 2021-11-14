import sys
input = sys.stdin.readline
a, b = map(int, input().split())
site = {}

for a in sys.stdin:
    a = a.split()
    if a[0] in site:
        print(site[a[0]])
    else:
        site[a[0]] = a[1]
# for _ in range(a):
#     k = input().split()
#     site[k[0]] = k[1]
#
# for _ in range(b):
#     print(site[input().split()[0]])
#
