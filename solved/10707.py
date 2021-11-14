arr = []
for _ in range(5):
    arr.append(int(input()))

print(min(arr[0]*arr[4], arr[1]+arr[3]*(arr[4]-arr[2]) if arr[4]>arr[2] else arr[1]))