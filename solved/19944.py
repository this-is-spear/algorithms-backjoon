a, b = map(int, input().split())
if b < 3:
    print('NEWBIE!')
elif b <= a:
    print('OLDBIE!')
else:
    print('TLE!')
