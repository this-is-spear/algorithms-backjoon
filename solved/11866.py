n, k = map(int,input().split())
arr = [i for i in range(1, n+1)]
answer = []
temp = k-1
while arr:
    answer.append(arr.pop(temp))
    temp += k-1
    if len(arr)>0:
        temp %= len(arr)
    else:
        break
print('<'+', '.join(str(i) for i in answer)+'>')
