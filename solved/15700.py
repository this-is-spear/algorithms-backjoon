a,b = map(int, input().split())
print((a*b-1)//2 if a*b%2 else a*b//2)