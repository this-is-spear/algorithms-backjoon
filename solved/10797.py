a = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in arr:
    if a == i:
        answer += 1
print(answer)
