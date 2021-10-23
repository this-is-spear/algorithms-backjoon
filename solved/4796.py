
i = 0
while True:
    i += 1
    arr = list(map(int, input().split()))
    if 0 in arr:
        break
    print("Case {0}: {1}".format(i, arr[0]*(arr[2]//arr[1]) + arr[2]%arr[1] if arr[0]>arr[2]%arr[1] else arr[0]*(arr[2]//arr[1]) + arr[0] ))
