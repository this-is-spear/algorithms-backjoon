r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(input()[1:-1].split("."))
answer = []
for i in arr:
    for k in i:
        if k != "":
            answer.append((int(k[0]), i.index(k)))
            break
answer.sort(key=lambda x: -x[1])
i = 0
d = -1
k = 0
a = [0] * 9
while i < len(answer):
    if d == -1:
        k += 1
        a[answer[i][0] - 1] = k
        d = answer[i][1]
    elif d == answer[i][1]:
        a[answer[i][0] - 1] = k
    else:
        k += 1
        a[answer[i][0] - 1] = k
        d = answer[i][1]
    i += 1
print('\n'.join([str(i) for i in a]))
