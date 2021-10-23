# m, n = map(int, input().split())
m, n = 1, 3
# arr = {i for i in range(2, n + 1)}
# for i in range(2, int(n ** 0.5) + 1):
#     for k in range(2 * i, n + 1, i):
#         arr -= {k}
# print('\n' .join([str(i) for i in sorted(arr) if i >= m]))
# for i in arr:
#     if i >= m:
#         print(i)

arr2 = [i for i in range(2, n + 1)]
for i in range(2, int(n ** 0.5) + 1):
    for k in range(2 * i, n + 1, i):
        if arr2[k - 2] != 0:
            arr2[k - 2] = 0
print('\n'.join(str(i) for i in arr2[(m - 2) if m > 2 else 0:] if i != 0))
