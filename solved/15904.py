import sys

input = sys.stdin.readline
arr = input()
print(arr)
t = 'UCPC'
temp = 0
for i in arr:
    if temp > 3:
        break
    if i == t[temp]:
        temp += 1
if temp == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
