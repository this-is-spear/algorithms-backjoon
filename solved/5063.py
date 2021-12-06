for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a+c < b:
        print('advertise')
    elif a+c == b:
        print('does not matter')
    else:
        print('do not advertise')