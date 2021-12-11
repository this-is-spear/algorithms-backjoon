a = 64
x = int(input())
answer = 0
for i in range(6, -1, -1):
    if x // 2**i:
        answer += (x//2**i)
        x -= (x//2**i)*(2 ** i)
print(answer)