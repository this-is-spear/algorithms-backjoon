while True:
    answer = 1
    a = input()
    if a == '0':
        break
    for i in a:
        if i == '1':
            answer += 3
        elif i == '0':
            answer += 5
        else:
            answer += 4
    else:
        print(answer)
