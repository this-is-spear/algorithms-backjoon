arr = []
ran = range(int(input()))
for _ in ran:
    a, b = map(int, input().split())
    arr.append((a, b))

d = []
for i in arr:
    count = 0
    for k in arr:
        if i[0] < k[0] and i[1] < k[1]:
            count += 1
    d.append(count + 1)
print(' '.join([str(i) for i in d]))