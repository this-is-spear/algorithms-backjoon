c, d = map(int, input().split())
a = [int(input()) for _ in range(c)]
d = sum(a)
lt, rt = 1, max(a)
while rt >= lt:
    mid = (lt + rt) // 2
    print(mid)
    if sum([i // mid for i in a]) < d:
        rt = mid - 1
    else:
        lt = mid + 1
print(rt)

