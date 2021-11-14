from sys import stdin
arr = []
input()
for a in map(str, stdin):
    if 'front' in a:
        print(-1 if not arr else arr[0])
    elif 'back' in a:
        print(-1 if not arr else arr[-1])
    elif 'size' in a:
        print(len(arr))
    elif 'empty' in a:
        print(0 if arr else 1)
    elif 'pop' in a:
        print(-1 if not arr else arr.pop(0))
    else:
        arr.append(a.split()[1])
