import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0]
for i in range(len(arr)):
    dp += [dp[i] + arr[i]]
for _ in range(m):
    i,k = map(int,input().split())
    print(dp[k] - dp[i-1])