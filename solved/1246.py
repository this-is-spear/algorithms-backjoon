n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
a.sort(reverse=True)
answer = (0, 0)
for i, k in enumerate(a):
    if answer[1] <= k * ((i + 1) if i + 1 <= n else n):
        answer = (k, (i + 1) * k)
print(answer[0], answer[1])
