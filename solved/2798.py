import itertools
a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr = [sum(i) for i in list(itertools.combinations(arr, 3))]
an = [i for i in arr if b >= i]
print(max(an))