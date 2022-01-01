a = int(input())
arr = list(map(int, input().split()))
temp = [0]*a
temp[0] = arr[0]
answer = arr[0]

for i in range(1, a):
    temp[i] = max(arr[i], temp[i-1]+arr[i])
    answer = max(answer, temp[i])

print(answer)