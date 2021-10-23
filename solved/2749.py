pisano = 1500000
t = int(input())%pisano
arr = [0, 1]
for i in range(2, pisano):
    arr.append((arr[i - 1] + arr[i - 2]) % 1000000)
print(arr[t])


