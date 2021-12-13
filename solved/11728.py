c = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(' '.join(str(i) for i in sorted(a + b)))
