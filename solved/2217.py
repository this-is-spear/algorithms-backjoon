a = []
for i in range(int(input())):
    a.append(int(input()))
a = sorted(a, reverse=True)
for i, k in enumerate(a):
    a[i] = (i+1)*a[i]
print(max(a))