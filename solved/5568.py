import collections
n = int(input())
k = int(input())
a = []
answer = dict()
for _ in range(n):
    a.append(input())
import itertools
for i in itertools.permutations(a, k):
    if ''.join(i) not in answer:
        answer[''.join(i)] = 0
    answer[''.join(i)] += 1
print(len(answer))