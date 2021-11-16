for _ in range(int(input())):
    i = int(input())
    dp = [0 for _ in range(i+1 if i>3 else 4)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for k in range(4,i+1):
        dp[k] = dp[k-1]+dp[k-2]+dp[k-3]
    print(dp[i])