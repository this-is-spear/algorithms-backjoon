
a = int(input())
arr = list(map(int, input().split()))
mon = int(input())

lt = 1
rt = max(arr)
while rt >= lt:
    mid = (rt + lt)//2
    if sum([mid if i > mid else i for i in arr]) > mon:
        rt = mid-1
    elif sum([mid if i > mid else i for i in arr]) < mon:
        lt = mid+1
    else:
        break
print((rt + lt)//2)
