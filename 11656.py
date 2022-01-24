
a = input()
arr = []
for i in range(len(a)):
    arr.append(a[i:])

for i in sorted(arr):
    print(i)

