n = int(input())
while True:
    k = int(input())
    if k == 0:
        break
    print('{0}{1}{2}.'.format(k,' is NOT a multiple of ' if k % n else ' is a multiple of ',n))