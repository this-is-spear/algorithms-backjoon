a = int(input())
if a == 0:
    print('divide by zero')
else:
    b = list(map(int,input().split()))
    answer = 0
    for i in b:
        answer += i/a
    print('{0:0.2f}'.format(round(sum(b)/a/answer,2)))
