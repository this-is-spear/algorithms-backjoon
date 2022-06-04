# # LIS 초기 값으로 첫 번째 수열의 값을 갖는다.
# # 만약 key가 LIS의 마지막 값보다 클 경우 추가해준다.
# # Lower Bound 이분탐색을 진행한다.
# # min value가 LIS에서 대치 될 원소의 위치가 될 것이고 해당 위치에 key값으로 원소를 바꿔준다.
# # 위 과정을 통해 나온 LIS의 길이를 출력한다.


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