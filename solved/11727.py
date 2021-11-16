i = int(input())
dp = [0 for _ in range(i+1 if i>1 else 3)]
dp[1] = 1
dp[2] = 3
for k in range(3, i+1):
    dp[k] = dp[k-1]+2*dp[k-2]
print(dp[i]%10007)