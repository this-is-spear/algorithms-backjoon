i = int(input())
dp = [0 for _ in range(i + 1)]
for k in range(1, i + 1):
    a, b, c = map(int, input().split())
    if k > 1:
        dp[k] = [min(a + dp[k - 1][1], a + dp[k - 1][2]), min(b + dp[k - 1][0], b + dp[k - 1][2]),
                 min(c + dp[k - 1][0], c + dp[k - 1][1])]
    else:
        dp[k] = [a, b, c]
print(min(dp[i]))
