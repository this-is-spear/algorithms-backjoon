import sys
input = sys.stdin.readline
a = int(input())
arr = list(map(int, input().split()))
arrk = [[0]*a for _ in range(a)]
for num_len in range(a):
    for start in range(a - num_len):
        end = start + num_len
        if start == end:
            arrk[start][end] = 1
        if arr[start] == arr[end]:
            if end > start+1:
                if arrk[start+1][end-1] == 1:
                    arrk[start][end] = 1
            else:
                arrk[start][end] = 1
for _ in range(int(input())):
    i,k = map(int,input().split())
    print(arrk[i-1][k-1])