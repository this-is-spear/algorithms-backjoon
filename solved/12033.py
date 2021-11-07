a = 0
for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    k = []
    while arr:
        i = arr.pop()
        k.append(i//4 * 3)
        arr.remove(i//4 * 3)
    a += 1
    print('Case #{0}:'.format(a), ' '.join([str(i) for i in sorted(k)]))