
arr = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0, 'Total':0}
a = []
while True:
    try:
        a = input().split()
        if len(a) == 0:
            break
        else:
            for i in a:
                if i in arr:
                    arr[i] += 1
                    arr['Total'] += 1
                else:
                    arr['Total'] += 1
    except:
        break

for i in arr.items():
    print('{0} {1} {2:.2f}'.format(i[0],i[1],round(i[1]/arr['Total'], 2)))
