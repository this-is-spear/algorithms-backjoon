i = int(input())
lt = 1
rt = i
while rt >= lt:
    mid = (rt+lt)//2
    if mid**2 == i:
        print(mid)
        break
    elif mid**2 >= i:
        rt = mid-1
    else:
        lt = mid+1
