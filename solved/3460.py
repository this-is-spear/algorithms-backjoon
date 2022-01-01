for _ in range(int(input())):
    a = int(input())
    answer = 0
    list = []
    while a > 0:
        a, b = divmod(a, 2)
        if b == 1:
            list.append(answer)
        answer += 1
    print(' '.join(str(i) for i in list))
