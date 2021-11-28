for _ in range(int(input())):
    a = int(input())
    dp = [0,1,1,1,2,2] + [0]*(a-5)
    for i in range(6,a+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[a])