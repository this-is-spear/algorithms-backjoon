# 1. 같은 눈 세 개 10000 + 1000 * x(같은 눈)
# 2. 같은 눈 두 개 1000 + 100 * x(같은 눈)
# 3. 다른 눈 중 가장 큰 x * 100.

answer = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        sum_int = 10000 + 1000 * a
    elif a == b or b == c or a == c:
        sum_int = 1000 + 100 * (a if a == b or a == c else c if c == b else b)
    else:
        sum_int = 100 * max(a, b, c)
    answer = max(answer, sum_int)
print(answer)
