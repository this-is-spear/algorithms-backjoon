
for _ in range(int(input())):
    temp_a = []
    for i in input():
        if i == '(':
            temp_a.append('(')
        else:
            if temp_a:
                temp_a.pop()
            else:
                print('NO')
                break
    else:
        print('YES' if not temp_a else 'NO')