# n = int(input())
# while n > 0:
#     if n == 1:
#         print()
#         break
#     for i in range(2, 10000000):
#         if (n/i).is_integer():
#             print(i)
#             n = n / i
#             break

n = int(input())
d = 2
while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 2 if d > 2 else 1
if n > 1:
    print(n)
