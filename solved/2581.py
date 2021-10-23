m = int(input())
n = int(input())
arr = {i for i in range(2, n+1)}
for i in range(2, int(n**0.5)+1):
    for k in range(2*i, n+1, i):
        arr -= {k}
arr = [i for i in arr if i >= m]
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
