a = int(input())
dp = [0]*(a+1 if a+1>3 else 2)
dp[1] = 5
temp = 2
while temp < a+1:
    dp[temp] = dp[temp-1] + temp*5 - 2 * temp + 1
    temp += 1
print(dp[a]%45678)