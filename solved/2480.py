arr = list(map(int, input().split()))

a = {}
for i in arr:
    a.setdefault(i, 0)
    a[i] += 1
a = sorted(a.items(), reverse=True)
for i in a:
    if i[1] == 3:
        print(10000 + i[0] * 1000)
        break
    elif i[1] == 2:
        print(1000 + i[0]*100)
        break
else:
    print(a[0][0]*100)
