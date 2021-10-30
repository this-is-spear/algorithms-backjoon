a, b = map(int,input().split())
arr = list(map(int,input().split()))

print(' '.join(str(i-a*b) for i in arr))