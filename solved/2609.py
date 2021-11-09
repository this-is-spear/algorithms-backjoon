# import math
a, b = map(int,input().split())

def gcd(a,b):
    a, b = max(a,b), min(a,b)
    while a%b != 0:
        a,b = a, a%b
    return b


print(gcd(a,b))
print(a*b//gcd(a,b))
