a = input()
if len(a) >= 3:
    if a[-2] != '0':
        print(int(a[:-2]) + int(a[-2:]))
    else:
        print(int(a[:-1]) + int(a[-1]))
else:
    print(int(a[-2])+int(a[-1]))