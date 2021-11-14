arr = []
sum = 0
temp = 0
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))