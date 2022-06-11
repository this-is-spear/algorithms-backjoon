size = int(input())

arr = [0] * (size if size != 1 else 2)
arr[0] = 1
arr[1] = 2

for i in range(2, size):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 15746

if size == 1:
    print(1)
else:
    print(arr[-1])
