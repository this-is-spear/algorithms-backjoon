import statistics

for _ in range(int(input())):
    a = list(map(int, input().split()))
    print("{:.3f}%".format(len([i for i in a[1:] if i > sum(a[1:]) / a[0]])/a[0]*100))
