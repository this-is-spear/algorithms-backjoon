answer = [0, 0]
for i in range(5):
    a = sum(map(int, input().split()))
    if a > answer[1]:
        answer = [i+1, a]
print(' '.join(str(i) for i in answer))