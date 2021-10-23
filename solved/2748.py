arr = [0, 1]
a = int(input())
for i in range(2, a+1):
    arr.append(arr[i-1] + arr[i-2])
print(arr[a])