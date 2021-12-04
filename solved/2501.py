import heapq
import sys
a,b = map(int,input().split())
arr = []
for i in range(int(a**.5)):
    if not a % (i + 1) :
        if i + 1 == a // (i + 1):
            heapq.heappush(arr, i + 1)
        else:
            heapq.heappush(arr, i+1)
            heapq.heappush(arr, a//(i+1))
for _ in range(b):
    try:
        item = heapq.heappop(arr)
    except:
        print(0)
        sys.exit(0)
else:
    print(item)
