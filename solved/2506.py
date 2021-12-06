a = int(input())
arr = map(int, input().split())
answer = 0
temp = 0
for i in arr:
    if i == 1:
        answer += 1
        if temp > 0:
            answer += temp
        temp += 1
    else:
        temp = 0
print(answer)