# 수를 받는다
plus = []
minus = []
for i in range(int(input())):
    a = int(input())
    if a > 0:
        plus.append(a)
    else:
        minus.append(a)
answer = 0
plus = sorted(plus)
minus = sorted(minus, reverse=True)
while plus:
    num = plus.pop()
    if len(plus) >= 1:
        try:
            a = plus.pop()
            if a*num > a+num:
                answer += num * a
            else:
                answer += num + a
        except:
            answer += num
    else:
        answer += num
while minus:
    num = minus.pop()
    if len(minus) >= 1:
        try:
            answer += num* minus.pop()
        except:
            answer += num
    else:
        answer += num
print(answer)

# 양수의 배열의 크기가 1보다 큰지 확인
# 크면 두개의 값을 꺼내와 두 값을 더한 값과 곱한 값을 체크
# 둘 중 큰 값을 정답에 더함
# 크기가 1개라면 하나의 값을 꺼내와 정답에 저장
# 크기가 0개라면 리턴
# 음수 저장
# 0 도 같이 처리
# 음수끼리 곱하면 양수로 변함
# 음수의 배열이의 크기가 1보다 큰지 확인
# 크다면 두개의 값을 꺼내와 곱해서 정답에 저장
# 1개라면 0이 있는지 확인하고 있다면 없애고 없다면 정담에서 그만큼 뺌
# 크기가 0개라면 바로 리턴
