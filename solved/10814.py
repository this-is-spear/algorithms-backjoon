arr = {}
k = []
for i in range(int(input())):
    # a, b = input().split()
    k.append(list(input().split()))
    # arr[b] = (int(a), i + 1)
# arr = sorted(arr.items(), key=lambda x: (x[1][0], x[1][1]))
# for i in arr:
#     print(i[1][0], i[0])

k.sort(key=lambda x:int(x[0]))
for i in range(len(k)):
    print(k[i][0], k[i][1])
