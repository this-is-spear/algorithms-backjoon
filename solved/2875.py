a,b,c = map(int,input().split())
k = min(a//2, b)
c -= a-k*2 + b-k
if c > 0:
    an = c//3+1 if c%3 else c//3
    print(k - an)
else:
    print(k)