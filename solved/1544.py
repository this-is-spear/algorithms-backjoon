arr = []
answer = 0
for i in range(int(input())):
    a = input()
    if a not in arr:
        answer += 1
        for i in range(len(a)):
            arr.append(a[i:]+a[:i])
print(answer)