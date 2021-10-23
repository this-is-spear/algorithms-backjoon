int(input())
a = sorted(map(int,input().split()))
print(sum([i * a[-i] for i in range(len(a), 0, -1)]))
