a = int(input())
arr = list(map(int, input().split()))
arr.sort()
if a == 1:
    print(arr[0]**2)
else:
    print(arr[0]*arr[-1])