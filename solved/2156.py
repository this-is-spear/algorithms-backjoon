n = int(input())
pool = [0 for _ in range(10005)]
for i in range(n):
    pool[i + 2] = int(input())
dp = [0 for _ in range(10005)]
dp[2] = pool[2]
for i in range(n-1):
    dp[i + 3] = max(dp[i + 2], dp[i + 1] + pool[i + 3], dp[i] + pool[i + 2] + pool[i + 3])
print(dp[n + 1])
