a,b,c = map(int,input().split())

if a+b+c >= 100:
    print('OK')
elif a == min(a,b,c):
    print('Soongsil')
elif b == min(a,b,c):
    print('Korea')
else:
    print('Hanyang')