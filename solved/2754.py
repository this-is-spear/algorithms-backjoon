import sys

a = input()
answer = 0.0

if a[0] == 'A':
    answer += 4
    pass
elif a[0] == 'B':
    answer += 3
    pass
elif a[0] == 'C':
    answer += 2
    pass
elif a[0] == 'D':
    answer += 1
    pass
else:
    print(answer)
    sys.exit(0)

if a[1] == '+':
    answer += 0.3
elif a[1] == '-':
    answer -= 0.3

print(answer)
