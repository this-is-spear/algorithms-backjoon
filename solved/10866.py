from sys import stdin
arr = []
input()
for a in map(str, stdin):
    if 'pop_front' in a:
        print(-1 if not arr else arr.pop(0))
    elif 'pop_back' in a:
        print(-1 if not arr else arr.pop())
    elif 'push_front' in a.split():
        arr.insert(0, a.split()[1])
    elif 'push_back' in a.split():
        arr.append(a.split()[1])
    elif 'front' in a:
        print(-1 if not arr else arr[0])
    elif 'back' in a:
        print(-1 if not arr else arr[-1])
    elif 'size' in a:
        print(len(arr))
    elif 'empty' in a:
        print(0 if arr else 1)
