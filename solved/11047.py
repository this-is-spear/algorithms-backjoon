n, k = map(int, input().split())
a = []
for i in range(int(n)):
    a.append(int(input()))
answer = 0
while k > 0:
    a_pop = a.pop()
    answer += k // a_pop
    k %= a_pop
print(answer)


# N, K = map(int, input().split())
#
# Coins = []
# for i in range(N) : Coins.append(int(input()))
#
#
# ans = 0
# while K > 0 :
#     coin = Coins.pop()
#     ans += K // coin
#     K %= coin
#
# print(ans)
#
