l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(l - max(a//c+1 if a%c else a//c, b//d+1 if b%d else b//d))