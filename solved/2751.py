import heapq
import sys
hq = []
for i in range(int(input())):
    heapq.heappush(hq, int(sys.stdin.readline()))

while hq:
    sys.stdout.write(str(heapq.heappop(hq)) +'\n')