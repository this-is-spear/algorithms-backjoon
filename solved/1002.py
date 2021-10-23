# def solution():
#     l = []
#     for i in range(int(input())):
#         x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
#         d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#         r = abs(r1 - r2) if d < min(r1, r2) else r1 + r2
#         if d > max(r1, r2): # 내접
#             r = abs(r1 - r2)
#             if (x1, y1) == (x2, y2) and r1 == r2:
#                 print(-1)
#             if r == d:
#                 print(1)
#             elif r < d:
#                 print(2)
#             else:
#                 print(0)
#         elif d < max(r1, r2):
#             r = r1 + r2
#             if r == d:
#                 print(1)
#             elif r > d:
#                 print(2)
#             else:
#                 print(0)
#         else:
#             print(2)
# exec(int(input()) * "print(sum(map(int,input().split())));")

def sol2(x1, y1, r1, x2, y2, r2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if max(r1, r2) > d:  # 내접
        print(-1 if (x1, y1, r1) == (x2, y2, r2) else 2 if abs(r1 - r2) < d else 0 if abs(r1 - r2) > d else 1)
    else:  # 외접
        print(2 if r1 + r2 > d else 0 if r1 + r2 < d else 1)


# exec(int(input()) * "x1, y1, r1, x2, y2, r2 = map(int,input().split());")
# d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# if max(r1, r2) > d:  # 내접
#     print(-1 if (x1, y1, r1) == (x2, y2, r2) else 2 if abs(r1 - r2) < d else 0 if abs(r1 - r2) > d else 1)
# else:  # 외접
#     print(2 if r1 + r2 > d else 0 if r1 + r2 < d else 1)

# for i in range(int(input())):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#     if max(r1, r2) > d:
#         print(-1 if (x1, y1, r1) == (x2, y2, r2) else 2 if abs(r1 - r2) < d else 0 if abs(r1 - r2) > d else 1)
#     else:
#         print(2 if r1 + r2 > d else 0 if r1 + r2 < d else 1)

sol2(0, 0, 13, 40, 0, 37)
sol2(0, 0, 3, 0, 7, 4)
sol2(1, 1, 1, 1, 1, 5)
# sol2(0, 0, 17, 40, 0, 33)

# 두 원간의 거리를 이용
# 두원의 거리와 각 원과의 거리 계산
# 만약 거리가 작은 원보다 작다면 원 하나가 다른 원 안에 들어가는 경우이다.
# 외접한다면 max(r1, r2) > distance
# 내접한다면 max(r1, r2) < distance
# 같다면
