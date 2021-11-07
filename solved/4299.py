a, b = map(int, input().split())
i = (a-b)//2
k = (a+b)//2
if i<0 or k<0 or i+k != a or k-i != b:
    print(-1)
else:
    print(max(i,k), min(i,k))