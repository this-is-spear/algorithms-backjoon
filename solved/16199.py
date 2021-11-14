arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

# 만 나이
if arr_2[0] > arr_1[0]:
    if arr_2[1] > arr_1[1]:
        print(arr_2[0] - arr_1[0])
    elif arr_2[1] == arr_1[1] and arr_2[2] >= arr_1[2]:
        print(arr_2[0] - arr_1[0])
    else:
        print(arr_2[0] - arr_1[0]-1)
else:
    print(0)
# 세는 나이
print(arr_2[0]-arr_1[0]+1)
# 연 나이
print(arr_2[0]-arr_1[0])
