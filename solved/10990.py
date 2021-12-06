a = int(input())

for i in range(1,a+1):
    if i > 1:
        print(' '*(a - i)+'*'+' '*(2*i-3)+ '*')
    else:
        print(' '*(a-i)+'*')