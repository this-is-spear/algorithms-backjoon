a = []
b = []

t = int(input())

for _ in range(t):
    i, k = map(int, input().split())
    i = i%10
    a.append(i)
    b.append(k)

# 1은 1
# 2는 2 4 8 6 2
# 3은 3 9 7 1 3
# 4는 4 6 4
# 5는 5
# 6은 6
# 7은 7 9 3 1 7
# 8은 8 4 2 6 8
# 9는 9 1 9

for i in range(t):
    if a[i] in [1, 5, 6]:
        print(a[i])
    elif a[i] == 2:
        print([2, 4, 8, 6][(b[i] - 1) % 4])
    elif a[i] == 3:
        print([3, 9, 7, 1][(b[i] - 1) % 4])
    elif a[i] == 4:
        print([4, 6][(b[i] - 1) % 2])
    elif a[i] == 7:
        print([7, 9, 3, 1][(b[i] - 1) % 4])
    elif a[i] == 8:
        print([8, 4, 2, 6][(b[i] - 1) % 4])
    elif a[i] == 9:
        print([9, 1][(b[i] - 1) % 2])
    else:
        print(10)
