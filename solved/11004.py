import sys
input = sys.stdin.readline
a,b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[b-1])