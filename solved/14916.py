a = int(input())
arr = [0, -1, 1, -1, 2, 1] + [0] * (a-5)
for i in range(6, a+1):
    if arr[i-2] == -1 and arr[i-5] == -1:
        arr[i] = -1
    if arr[i-2] == -1:
        arr[i] = arr[i-5] + 1
    elif arr[i-5] == -1:
        arr[i] = arr[i-2] + 1
    else:
        arr[i] = min(arr[i-2], arr[i-5]) + 1
print(arr[a])