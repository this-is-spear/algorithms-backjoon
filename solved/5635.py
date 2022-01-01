arr = {}
for _ in range(int(input())):
    a,b,c,d = input().split()
    arr[a] = d+'{0:0>2}'.format(int(c))+'{0:0>2}'.format(int(b))
arr = sorted(arr.items(), key=lambda x:x[1])
print(arr[-1][0])
print(arr[0][0])