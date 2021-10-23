x, y = map(int, input().split())
lt = 0
rt = 1000000000
answer = 0
while rt >= lt:
    mid = (lt+rt)//2
    if int((mid+y)*100/(x+mid)) >= int(y*100/x)+1:
        answer = mid
        rt = mid-1
    else:
        lt = mid+1
print(answer if answer != 0 else -1)
