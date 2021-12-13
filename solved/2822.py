arr = {}
for i in range(1,9):
    arr[i] = int(input())
arr = sorted(arr.items(),reverse=True, key=lambda x:x[1])[:5]
arr.sort()
answer = 0
i = []
for k in arr:
    answer += k[1]
    i += [k[0]]
print(answer)
print(' '.join(str(k) for k in i))