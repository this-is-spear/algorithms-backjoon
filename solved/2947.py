arr = list(map(int, input().split()))

while True:
    an = 0
    for i in range(4):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            print(' '.join(str(i) for i in arr))
            an += 1
    if an == 0:
        break

