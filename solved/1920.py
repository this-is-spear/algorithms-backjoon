input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))
a = sorted(a)
for i in b:
    lt = 0
    rt = len(a) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] == i:
            print(1)
            break
        elif a[mid] > i:
            rt = mid - 1
        else:
            lt = mid + 1
    else:
        print(0)
