arr = []
for i in range(5):
    a = int(input())
    arr.append(a if a>=40 else 40)
print(sum(arr)//5)