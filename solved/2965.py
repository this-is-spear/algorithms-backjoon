a, b, c = map(int, input().split())
answer = 0
while True:
    if c - b > 1 and c - b > b - a:
        answer += 1
        a, b, c = b, c - 1, c
    elif b - a > 1 and b - a >= c - b:
        answer += 1
        a, b, c = a, a + 1, b
    else:
        break
print(answer)
