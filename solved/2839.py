# 몫, 나머지
# a, b = divmod(int(input()), 5)
a = int(input())
k = a // 5
while k >= 0:
    if ((a - k * 5) / 3).is_integer():
        break
    k -= 1
print((k + (a - k * 5) // 3) if k >= 0 else -1)
