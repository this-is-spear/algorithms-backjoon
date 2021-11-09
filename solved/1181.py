arr = []
for i in range(int(input())):
    a = input()
    if a not in arr:
        arr.append(a)
arr.sort(key=lambda x:(len(x), x))
print('\n'.join([i for i in arr]))