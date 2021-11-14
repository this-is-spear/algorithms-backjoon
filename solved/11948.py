answer = []
for _ in range(6):
    answer.append(int(input()))
an = sorted(answer[:4], reverse=True)
print(sum(an[:3])+max(answer[4], answer[5]))
