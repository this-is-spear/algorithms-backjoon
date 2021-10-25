input()
arr = list(map(int, input().split()))
arr.sort(reverse=True)
answer = 0
temp = 0
for i in range(len(arr)):
    arr[i] = arr[i] + i + 1
print(max(arr)+1)

