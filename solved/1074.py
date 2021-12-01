n, r, c = map(int, input().split())
i = 1
while max(r, c) > 2 ** i:
    i *= 2
answer = 0
while True:
    temp_2 = 2**i
    temp_1 = 2**(2*i)
    if r - temp_2 >= 0:
        r -= temp_2
        answer += temp_1*2
    if c - temp_2 >= 0:
        c -= temp_2
        answer += temp_1
    if i == 0:
        break
    i -= 1
print(answer)
