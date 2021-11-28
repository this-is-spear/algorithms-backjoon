input()
arr = map(int, input().split())
temp_1 = 0
temp_2 = 0
for i in arr:
    temp_1 += (i // 30) * 10 + 10
    temp_2 += (i // 60) * 15 + 15

if temp_1 > temp_2:
    print('M', temp_2)
elif temp_2 > temp_1:
    print('Y', temp_1)
else:
    print('Y', 'M', temp_1)
