a = input()
a = 'abcdefghijalmnopqrstuvwxyz'
answer = [-1]*26
for index, _ in enumerate(a):
    t = a.find(a[index])
    answer[t] = index if answer[t] == -1 else answer[t]
print(' '.join([str(i) for i in answer]))