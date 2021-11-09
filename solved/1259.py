while True:
    a = input()
    if a == '0':
        break
    for i in range(1, len(a) // 2+1):
        if a[i-1] is not a[-i]:
            print('no')
            break
    else:
        print('yes')
