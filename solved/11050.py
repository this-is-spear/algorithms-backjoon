from math import factorial

n, k = map(int, input().split())
if n >= k >= 0:
    print(int(factorial(n)/(factorial(k)*factorial(n-k))))
else:
    print(0)