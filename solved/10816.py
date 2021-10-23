from collections import Counter
import sys
input = sys.stdin.readline
_, a, _ = input(), Counter(input().split()), input()
print(' '.join('1' if a[i] != 0 else '0' for i in input().split()))