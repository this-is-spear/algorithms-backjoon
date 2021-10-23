# 배열 다 저장

# 가장 작은 가방을 가져와 그 가방에 크기에 맞거나 크기보다 작은 수를 저장
# 가득 차면 그 다음 큰 가방을 가져와 크기에 맞거나 크기보다 작은 수를 저장
# 가방을 다 사용하거나 보석이 다 떨어질 때까지 리턴

# 주의 사항
# 어떤 컬렉션으로 저장해야 같은 무게에 같은 가격인 보석을 처리할 수 있는가?
# 각 0으로 표시한다음 그 인덱스에 저장하는 방법은 같은 무게나 같은 가격인 보석을 처리할 수 없음
# 딕셔너리도 키값이 중복이 되서 불가능
# 캡슐화해서 가능한가?
# 캡술화 (x1, x2)로 해서 무게는 오름차순, 가치는 내림차순으로 만든다.
# bs 안에 제일 작은 가방을 가져온다.
# jv 중에 bs에서 가져온 가방무게 보다 작은 보석중 가장 가치있는 보석을 꺼내온다.
# 두개 이상 넣지 못하기 때문에 두개 합하거나 다 넣은 값의 최대값을 구할 필요 없다.

# import heapq
# a, b = map(int, input().split())
# jv = []
# bs = []
# an = []
# answer = 0
# for _ in range(a):
#     s, p = map(int, input().split())
#     jv.append((s, p))
# for _ in range(b):
#     bs.append(int(input()))
#
# jv = sorted(jv, key=lambda x: (x[0], -x[1]))
# bs = sorted(bs, reverse=True)
#
# while jv and bs:
#     end = bs.pop()
#     for i in range(len(jv)):
#         if end < jv[i][0]:
#             if len(an):
#                 answer += heapq.heappop(an)[1]
#             break
#         else:
#             heapq.heappush(an, (-jv[i][1], jv[i][1]))
#     jv = jv[i+1:]
# # 이렇게 되면 jv가 먼저 끝나는 경우에 an이 남는다 bs가 남는 수만큼 an에서 앞에 있는 값을 꺼내 온다.
# # bs 가 남아도 an에 값이 없는 경우는 방금까지 더한 answer의 값을 리턴 해준다.
# for i in range(len(bs)):
#     if len(an):
#         answer += heapq.heappop(an)[1]
# print(answer)


import heapq
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
jList = [list(map(int, input().split())) for _ in range(n)]
bList = [int(input()) for _ in range(k)]
jList.sort()
bList.sort()
answer = 0
temp = []
for bWeight in bList:
    while jList and bWeight >= jList[0][0]:
        heapq.heappush(temp, -jList[0][1])
        heapq.heappop(jList)
    if temp:
        answer += heapq.heappop(temp)
    elif not jList:
        break
print(-answer)
