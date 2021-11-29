sum_i = 0
min_i = 100
for _ in range(7):
    a = int(input())
    if a%2:
        sum_i += a
        min_i = min(min_i, a)

if min_i == 100:
    print(-1)
else:
    print(sum_i)
    print(min_i)

