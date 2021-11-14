arr = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append((a, b))
print('\n'.join(str(i[0]) + ' ' + str(i[1]) for i in sorted(arr, key=lambda x: (x[1], x[0]))))
