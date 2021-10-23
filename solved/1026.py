int(input())
a = sorted(map(int,input().split()), reverse=True)
b = sorted(map(int,input().split()))
k = sum([a[i] * b[i] for i in range(len(a))])
print(k)

# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# def min(A,B):
#     sum = 0
#     A.sort()
#     for i in A:
#         t = max(B)
#         sum += i*t
#         B.pop(B.index(t))
#     return print(sum)
# min(A,B)