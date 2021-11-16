for _ in range(int(input())):
    i = int(input())
    dp = [[0, 0] for _ in range(i + 1)]

    dp[0] = [1, 0]
    if len(dp)>1:
        dp[1] = [0, 1]
    for i in range(2, len(dp)):
        dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]
    print(' '.join(str(i) for i in dp[i]))
