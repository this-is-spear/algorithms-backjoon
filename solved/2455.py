answer = 0
total_member = 0
for _ in range(4):
    a,b = map(int,input().split())
    total_member -= a
    total_member += b
    answer = max(answer, total_member)

print(answer)