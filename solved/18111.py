# 높은 층 전부 다 한층씩 깍던가
# 낮은 층 전부 다 한층씩 내리던가
# 가지고 있는 땅의 개수는 한정적
# 올리는게 더 짧게 걸림
# 가장 낮은 층으로 동결 or 가장 높은 층으로 동결
# 배열을 입력 받는다.
# 배열의 가장 낮은 층과 높은 층을 따로 저장한다.
# 모든 층의 개수를 다 더한 것과 그 크기에 가장 높은 층만큼 쌓은 크기의 차이를 구한다.
# 가지고 있는 땅의 개수와 비교한다.
# 가장 낮은 층을 구한 값과 가장 높은 층을 구한 값은 비교한다.
# 생각해보니 중간값도 있는데?!

n, m, b = map(int, input().split())
di = {}
for _ in range(n):
    k = list(map(int, input().split()))
    for i in k:
        di.setdefault(i, 0)
        di[i] += 1
answer = [0,0]
sum_i = sum(i[0]*i[1] for i in di.items())
for i in range(min(di.keys()), max(di.keys())+1):
    if n*m*i - sum_i <= b:
        an = 0
        for k in di.items():
            if k[0] < i:
                an += (i - k[0]) * k[1]
            elif k[0] > i:
                an += 2*(k[0] - i) * k[1]
        else:
            if answer[0] == 0:
                answer = [an,i]
            elif answer[0] >= an:
                answer = [an, i]
print(' '.join(str(i) for i in answer))