
a = int(input())
arr = []
for _ in range(a):
    a,b = map(int,input().split())
    arr.append([a,b])

item = 1
while arr:
    items = arr.pop(0)
    if item in items:
        item = items[1] if items[1] != item else items[0]
if 0 < item < 4:
    print(item)
else:
    print(-1)