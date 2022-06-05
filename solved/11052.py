
# 0. 첫 번째 숫자는 그대로 진행하고, 두 번째 숫자는 첫 번째 숫자와 비교해 큰 값으로 대치한다.
# 1. 3 번 째 이상인 n이라는 숫자를 비교한다.
#   1-1. 0부터 n//2 만큼만 조회한다.
# 2. 큰 값으로 대치한다.
# 3. 1번과 2번을 반복한다.
# 4. 마지막까지 조회한다.

a = int(input())
dp = list(map(int, input().rsplit()))

for i in range(1, a):
    for k in range(i // 2 + 1):
        dp[i] = max(dp[i], dp[k] + dp[i - k - 1])

print(dp[-1])
