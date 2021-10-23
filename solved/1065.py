
# 1의 자리는 모두 한수
# 2의 자리도 한수 100까지는 총 99개
# 3의 자리는 한수의 개수가 제각각

a = int(input())
if a >= 100:
    answer = 0
    title = 100
    while title <= a:
        index1 = [int(i) for i in str(title)]
        if index1[0]-index1[1] == index1[-2]-index1[-1]:
            answer += 1
        title += 1
    print(99+answer)
else:
    print(a)