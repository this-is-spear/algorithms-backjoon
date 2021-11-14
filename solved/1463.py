# n = int(input())
# dp = [0 for _ in range(n+1)]
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1
#     if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
#         dp[i] = dp[i // 2] + 1
#     if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
#         dp[i] = dp[i // 3] + 1
# print(dp[n])

# dp
def dp(n):
    if n in memo:
        return memo[n]
    # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
    # 이 경우를 나머지로 더해주는 것으로 짐작된다.
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
    memo[n] = m
    return m


memo = {1: 0, 2: 1}
n = int(input())
print(dp(n))