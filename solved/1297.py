c,a,b = map(int,input().split())

x = (c**2*a**2/(a**2 + b**2))**.5
y = (c**2*b**2/(a**2 + b**2))**.5
print(int(x), int(y))
