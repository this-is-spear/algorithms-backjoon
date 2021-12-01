import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    hq = []
    max_hq = []
    a = int(input())
    visited = [False for _ in range(1000000+1)]
    for i in range(a):
        s, k = map(str, input().split())
        if s == 'I':
            k = int(k)
            heapq.heappush(hq, (k, i))
            heapq.heappush(max_hq, (-k, i))
            visited[i] = True
        elif k == '1':
            while max_hq and not visited[max_hq[0][1]]:
                heapq.heappop(max_hq)
            if max_hq:
                visited[max_hq[0][1]] = False
                heapq.heappop(max_hq)
        else:
            while hq and not visited[hq[0][1]]:
                heapq.heappop(hq)
            if hq:
                visited[hq[0][1]] = False
                heapq.heappop(hq)
    else:
        while hq and not visited[hq[0][1]]: heapq.heappop(hq)
        while max_hq and not visited[max_hq[0][1]]: heapq.heappop(max_hq)
        print(f'{-max_hq[0][0]} {hq[0][0]}' if max_hq and hq else 'EMPTY')
