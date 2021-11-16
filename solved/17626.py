i = int(input())
dp = [0] * (i+1)
dp[1] = 1
for k in range(2, i+1):
    tt = 4
    print(int(k**.5))
    for t in range(int((k//2)**.5), int(k**.5)+1):
        if dp[k - t**2] + 1 == 1:
            tt = 1
            break
        tt = min(dp[k - t**2] + 1, tt)
    dp[k] = tt
print(dp[i])
