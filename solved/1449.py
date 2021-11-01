n,l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer =  0
while arr:
    answer += 1
    arr_pop = arr.pop(0)
    while arr:
        if arr_pop + l > arr[0]:
            arr.pop(0)
        else:
            break
print(answer)
