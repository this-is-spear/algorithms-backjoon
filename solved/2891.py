# a, b, c = map(int, input().split())
# a = [1] * a
# b = map(int, input().split())
# c = map(int, input().split())
# for i in b:
#     a[i - 1] -= 1
# for i in c:
#     a[i - 1] += 1
# answer = 0
# print(a)
# for i, k in enumerate(a):
#     if k == 2:
#         if i + 1 < len(a):
#             if a[i + 1] == 0:
#                 a[i + 1] += 1
#                 a[i] -= 1
#         elif i != 0:
#             if a[i - 1] == 0:
#                 a[i - 1] += 1
#                 a[i] -= 1
#     if k == 0:
#         if i + 1 < len(a):
#             if a[i + 1] == 2:
#                 a[i + 1] -= 1
#                 a[i] += 1
#             else:
#                 answer += 1
#         elif i != 0:
#             if a[i - 1] == 2:
#                 a[i - 1] -= 1
#                 a[i] += 1
#             else:
#                 answer += 1
#         else:
#             answer += 1
# print(a)

a, b, c = map(int, input().split())
a = [1] * a
b = map(int, input().split())
c = map(int, input().split())
for i in b:
    a[i - 1] -= 1
for i in c:
    a[i - 1] += 1
for i, k in enumerate(a):
    if i + 1 < len(a):
        if k == 2:
            if a[i+1] == 0:
                a[i+1] += 1
                a[i] -= 1
        if k == 0:
            if a[i+1] == 2:
                a[i+1] -= 1
                a[i] += 1
print(a.count(0))