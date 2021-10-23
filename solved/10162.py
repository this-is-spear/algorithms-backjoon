k = int(input())
print(k%10)
if k % 10:
    print(-1)
else:
    an = []
    arr = [10, 60, 300]
    while arr:
        arr_pop = arr.pop()
        an.append(k // arr_pop)
        k %= arr_pop
    print(' '.join([str(i) for i in an]))
