import sys
import heapq

input = sys.stdin.readline

size = int(input())
arr = []
for i in range(size):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()
result = []
heapq.heappush(result, arr[0][1])

for i in range(1, size):
    if arr[i][0] < result[0]:
        heapq.heappush(result, arr[i][1])
    else:
        heapq.heappop(result)
        heapq.heappush(result, arr[i][1])

print(len(result))
