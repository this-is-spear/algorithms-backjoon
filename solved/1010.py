import math
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    print(int(math.factorial(max(arr))/(math.factorial(min(arr))*math.factorial(max(arr)- min(arr)))))
