index = int(input())
arr = list(map(int, input().split()))
arrk = [1]*index
answer = 1
for i in range(index):
    temp = []
    for k in range(len(arr[:i])):
        if arr[k] < arr[i]:
            temp.append(arrk[k])
    if temp:
        arrk[i] = max(temp)+1
        answer = max(arrk[i], answer)
print(answer)