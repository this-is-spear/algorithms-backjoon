# from collections import defaultdict
# arr = defaultdict(str)
# for _ in range(int(input())):
#     a, b = input().split()
#     if b == 'enter':
#         arr[a] = b
#     else:
#         del arr[a]
# print('\n'.join([i for i in sorted(arr.keys(), reverse=True)]))

import sys
read = sys.stdin.readline

d = {}
for _ in range(int(read())):
    name, action = read().split()
    if action == 'enter':
        d[name] = True
    elif action == 'leave':
        if name in d:
            del d[name]
print('\n'.join(sorted(d.keys(), reverse=True)))