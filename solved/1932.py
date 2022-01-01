import sys
input = sys.stdin.readline
k = []
for i in range(int(input())):
    arr = list(map(int,input().split()))
    if i == 0:
        k = arr
    else:
        i + 1
        temp = []
        for t in range(i+1):
            if t == 0:
                temp.append(arr[0] + k[0])
            elif t == i:
                temp.append(arr[-1] + k[-1])
            else:
                temp.append(max(k[t-1]+arr[t], k[t]+arr[t]))
        k = temp

print(max(k))