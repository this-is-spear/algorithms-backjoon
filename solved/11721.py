a = 'BaeajoonOnlineJudge'
a = 'OneTwoThreeFourFiveSixSevenEightNineTen'
for i in a[0::10]:
    print(i)

n = input()
for i in range(0, len(n), 10):
    print(n[i:i + 10])
