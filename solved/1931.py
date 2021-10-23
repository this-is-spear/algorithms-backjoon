a = []
for i in range(int(input())):
    b, c = map(int, input().split())
    a.append((b, c))
answer = 0
last_k = 0
for i, k in sorted(a, key=lambda x: (x[1], x[0])):
    if last_k <= i:
        last_k = k
        answer += 1

print(answer)
