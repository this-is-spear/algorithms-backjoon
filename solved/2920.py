a = list(map(int, input().split()))
if [i for i in range(1,9)] == a:
    print('ascending')
elif [i for i in range(8,0,-1)] == a:
    print('descending')
else:
    print('mixed')