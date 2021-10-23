# 1 층 3 호
# 1*1 2*1 3*1
# if 2 층 3 호 이면
# 1*3 2*2 3*1 -> 1 1+2 1+2+3
# 3층 3호
# 1*6 2*3 3*1 -> 1 1+1+2 1+1+1+2+2+3
# 1*10 2*4 3*1 --> 1 1+1+1+2 1+1+1+1+1+1+2+2+2+3
# 재귀함수는 불가능
# def solution(k, n):
#     if k == 0:
#         return n
#     else:
#         return sum([solution(k-1, i) for i in range(1, n+1)])
#
# for i in range(int(input())):
#     k = int(input())
#     n = int(input())
#     print(solution(k,n))
#
#
# def solution2(k, n):
#     if k == 0:
#         return 1
#     elif n == 0:
#         return n
#     return solution2(k - 1, n) + solution2(k, n - 1)
# for i in range(int(input())):
#     k = int(input()) + 1
#     n = int(input())
#     print(solution2(k, n))

def solution(k, n):
    f = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(n-1):
            f[i+1] += f[i]
    print(f[-1])

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(solution(k, n))
