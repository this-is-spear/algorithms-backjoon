one_line = 'WB' * 4
ohter_line = 'BW' * 4
a_k = [1, 0]
b_k = [0, 1]
a, b = map(int, input().split())
arr = []
for _ in range(a):
    key = input()
    arr.append(key)
answer = 2500
for i in range(b - 7):
    for k in range(a - 7):
        # i,k 부터 i+7, k+7까지 모두 확인해야한다.
        # i,k부터 i, k+7 까지는 각자 확인하는 것을 8번 돌린다.
        # W부터 시작하는 값과 B부터 시작하는 값을 확인한다?
        # (1,0) (0,1) 이걸로 해결해야 하지 않을까?
        one_different = 0
        for index in range(8):
            line = one_line * a_k[index % 2] + ohter_line * b_k[index % 2]
            # compare
            for one_char in range(8):
                if arr[k+index][i:i+8] == line:
                    break
                if arr[k+index][i:i+8][one_char] == line[one_char]:
                    pass
                else:
                    one_different += 1

        two_different = 0
        for index in range(8):
            line = one_line * b_k[index % 2] + ohter_line * a_k[index % 2]
            # compare
            for one_char in range(8):
                if arr[k + index][i:i + 8] == line:
                    break
                if arr[k + index][i:i + 8][one_char] == line[one_char]:
                    pass
                else:
                    two_different += 1
        if answer > min(one_different, two_different):
            answer = min(one_different, two_different)
print(answer)