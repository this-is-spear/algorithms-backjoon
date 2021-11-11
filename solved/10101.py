arr = ['Equilateral', 'Isosceles', 'Scalene', 'Error']
re_arr = []
for i in range(3):
    re_arr.append(int(input()))

if re_arr.count(60) == 3:
    print(arr[0])
elif len(re_arr) != len(set(re_arr)) and sum(re_arr) == 180:
    print(arr[1])
elif sum(re_arr) == 180:
    print(arr[2])
else:
    print(arr[3])