# a = sorted(, reverse=True)
# for k in range(len(a)):
#     if k + 1 < len(a):
#         i += 1
#     an += i * a[k] if i != 0 else a[k]
# print(an)
# 위에 방법 틀림
# 두개 더해서 다음 거하고 비교 했을 때 커버리면 실패
# 아!
# 앞에 두개의 숫자하고 뒤에있는 세개의 숫자를 비교해서 계속 더해주면 된다!!

import heapq
heap = []
for _ in range(int(input())):
    heapq.heappush(heap, int(input()))
an = 0
while len(heap) > 1:
    a = heapq.heappop(heap) + heapq.heappop(heap)
    an += a
    heapq.heappush(heap, a)
print(an)
