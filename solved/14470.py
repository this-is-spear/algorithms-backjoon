arr = []
for _ in range(5):
    arr.append(int(input()))
answer = 0
if arr[0] < 0:
    answer += abs(arr[0]) * arr[2]
    answer += arr[3]
    arr[0] = 0
answer += arr[4] * (arr[1] - arr[0])
print(answer)