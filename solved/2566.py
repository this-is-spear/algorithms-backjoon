answer = 0
i = 0
k = 0
for temp in range(9):
    arr = list(map(int, input().split()))
    if answer < max(arr):
        answer = max(arr)
        i = temp
        k = arr.index(max(arr))

print(answer)
print(i+1, k+1)