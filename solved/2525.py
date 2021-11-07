a, b = map(int, input().split())
c = int(input())

if b + c >= 60:
    a += (b+c)//60
    b = (b+c)%60
if a >= 24:
    a %= 24
print(a, b)
# print(a + (b+c)//60 if not a + (b+c)//60 >= 24 else (a + (b+c)//60)%24, (b+c)%60)