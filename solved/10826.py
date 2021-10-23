a,b = 0,0
for k in range(int(input())+1):
    if k == 1 or k == 2:
        a, b = 0, 1
    elif k == 3:
        a, b = 1, 1
    else:
        a, b = a + b, a
print(a+b)