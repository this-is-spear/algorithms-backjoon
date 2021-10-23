
i = input().lower()
answer = 0
for a in i:
    if ord(a) <= 111:
        answer += (ord(a) - ord('a'))//3 + 3
    elif a in 'pqrs':
        answer += 8
    elif a in 'tuv':
        answer += 9
    else:
        answer += 10
print(answer)
