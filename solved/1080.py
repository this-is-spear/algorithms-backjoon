# 첫 째 행렬과 두번 째 행렬의 차이만큼 구한다.
# 3by3 행렬을 이용해 왼쪽 위에서부터 계속 바꾼다.
# 제일 오른쪽의 값이 변경되지 않으면 실패

# 본 행렬이 3by3 행렬이 아니라면 모두다 같은 수거나 모두 다 다른 수명 true 아니면 false
a, b = map(int, input().split())
fst_arr = []
for i in range(a):
    fst_arr.append(list(input()))
scd_arr = []
for i in range(a):
    scd_arr.append(list(input()))
an_arr = [[False] * b for i in range(a)]
for i in range(a):
    for k in range(b):
        if fst_arr[i][k] == scd_arr[i][k]:
            an_arr[i][k] = True
if a < 3 or b < 3:
    if fst_arr == scd_arr:
        print(0)
    else:
        print(-1)
    exit(0)

answer = 0
ifTrue = True
for i in range(len(an_arr) - 2):
    for k in range(len(an_arr[0]) - 2):
        if not an_arr[i][k]:
            answer += 1
            for it in range(3):
                for ki in range(3):
                    an_arr[i + it][k + ki] = True if an_arr[i + it][k + ki] == False else False
for i in an_arr:
    if False in i:
        ifTrue = False
        break
if ifTrue:
    print(answer)
else:
    print(-1)
