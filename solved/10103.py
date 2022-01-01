answer = [100,100]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a>b:
        answer[1] -= a
    elif a<b:
        answer[0] -= b

print('\n'.join(str(i) for i in answer))