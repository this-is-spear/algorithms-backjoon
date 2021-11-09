r = 31
M = 1234567891
k = int(input())
a = input()
answer = 0
for i in range(k):
    answer += (ord(a[i]) - ord('a') + 1)*r**i
print(answer%M)