import sys
input = sys.stdin.readline
a = int(input())
arr = [0]*a
for i in range(a):
    arr[i] = int(input())

arr.sort(reverse=True)
print('\n'.join(str(i) for i in arr))