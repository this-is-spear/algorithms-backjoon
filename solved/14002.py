import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rsplit()))
lis = [a[0]]
ans = 1

for num in a[1:]:
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        index = bisect_left(lis, num)
        lis[index] = num
print(ans)
print(' '.join(str(i) for i in lis))
