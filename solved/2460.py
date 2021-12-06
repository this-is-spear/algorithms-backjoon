answer = 0
sum_man = 0
for _ in range(10):
    a,b = map(int,input().split())
    sum_man += b - a
    answer = max(answer, sum_man)
print(answer)