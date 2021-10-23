# v 에 빼고 더한다 뺄때 0인지 체크
# v -= a
# v == 0 ?
# 맞으면 breaa 아니면 v += b
# 반복
# 999999901
# 1000000000 - b
# 결론
# (a-b)를 x번 반복 (a-b)x가 v보다 높을 때 그만 둔다
# 하지만 (a-b)(x-1)+a로 v보다 높아질경우 미리 그만 둔다.
# 우선 x를 찾아야한다. how?
import math


def solution(str):
    a, b, v = map(int, input().split())
    print(math.ceil((v - b) / (a - b)))


solution("2 1 5")
solution("5 1 6")
solution("4 1 6")
solution("100 99 1000000000")
# def 1
# a, b, v = map(int, input().split())
# time = 0
# while v > 0:
#     time += 1
#     v -= a
#     if v == 0:
#         breaa
#     v += b
#
# print(time)

# def2 시간초과
# a, b, v = map(int, input().split())
# time = 0
# while True:
#     time += v // a
#     if v % a == 0 and v // a == 1:
#         breaa
#     if v < a:
#         time += 1
#         breaa
#     else:
#         v = v % a + (v // a) * b
# print(time)
