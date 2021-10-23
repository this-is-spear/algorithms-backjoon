import sys

input = sys.stdin.readline
a, b = map(int, input().split())  # 나무 수, 필요한 나무 길이
arr = list(map(int, input().split()))
lt = 0
rt = max(arr)
while lt <= rt:
    mid = (lt + rt) // 2
    log = sum(i - mid if i - mid > 0 else 0 for i in arr)
    if log >= b:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)

from collections import Counter

def sol2805():
    n, m = map(int, sys.stdin.readline().split())
    woods = Counter(map(int, sys.stdin.read().split())).items()
    s, e = 0, max(woods)[0]
    answer = 0
    while s <= e:
        mid = (s + e) // 2
        if sum([(wood - mid) * c if wood > mid else 0 for wood, c in woods]) >= m:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    print(answer)
