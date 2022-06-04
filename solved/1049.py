# 필요로 하는 개수보다 많이 사야하고, 가장 적은 비용이어야 한다.
# 필요로 하는 개수는 100 이하 자연수이고, 비교 갯수는 50 이하 자연수이다. 가격은 0이상 1000 이하이다.
# 20개가 필요하다면
# 6 + 6 + 6 + 6
# 6 + 6 + 6 + 1 * 2
# 6 + 6 + 1 * 6 + 1 * 2
#
# 1. 6개 값 중 가장 싼 값을 고르고, 하나의 값중 가장 싼 값을 고른다.
# 2. 6과 1*6 중 싼 값을 고른다.
# 3. 6이 더 싼 경우 나머지 숫자를 어떻게 해결할지 결정한다.
# 4. 1*6이 싼 경우 낱개로 다 사버린다.

SIX = 6
a, b = map(int, input().split())
six_val, one_val = 1000, 1000

for _ in range(b):
    c, d = map(int, input().split())
    six_val = min(c, six_val)
    one_val = min(d, one_val)

if six_val < one_val * SIX:
    if a % SIX * one_val > six_val:
        print((a // SIX + 1) * six_val)
    else:
        print(a // SIX * six_val + a % SIX * one_val)
else:
    print(a * one_val)
