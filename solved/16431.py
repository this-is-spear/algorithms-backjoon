b = list(map(int, input().split()))
d = list(map(int, input().split()))
j = list(map(int, input().split()))
arr = [0, 0]
if abs(j[0] - b[0]) > 0 and abs(j[1] - b[1]) > 0:
    arr[0] = min(abs(j[0] - b[0]), abs(j[1] - b[1]))
    b[0] = b[0] - arr[0] if b[0] > j[0] else b[0] + arr[0]
    b[1] = b[1] - arr[0] if b[1] > j[1] else b[0] + arr[0]
if abs(j[0] - b[0]) > 0 or abs(j[1] - b[1]) > 0:
    arr[0] += abs(j[0] - b[0]) + abs(j[1] - b[1])
if abs(j[0] - d[0]) > 0 or abs(j[1] - d[1]) > 0:
    arr[1] = abs(j[0] - d[0]) + abs(j[1] - d[1])
if arr[0] < arr[1]:
    print('bessie')
elif arr[0] > arr[1]:
    print('daisy')


else:
    print('tie')
