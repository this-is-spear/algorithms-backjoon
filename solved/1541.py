# a - b - c
# a - ( b - c )
# (a - b) - c
# 5 1 2 5 8 2
# - 만 존재하면 순서대로 + 존재하면 + 먼저 해야함

a = list(input())
int_a = ""
a_int = []
a_sign = []
while a:
    a_pop = a.pop(0)
    if a_pop in "+-":
        a_int.append(int(int_a))
        a_sign.append(a_pop)
        int_a = ""
    else:
        int_a += a_pop
else:
    a_int.append(int(int_a))

def a(s):
    while a_sign.count(s):
        a_int[a_sign.index(s)] += a_int[a_sign.index(s) + 1] if s == "+" else -a_int[a_sign.index(s) + 1]
        a_int.pop(a_sign.index(s) + 1)
        a_sign.pop(a_sign.index(s))

a("+")
a("-")
print(a_int[0])

# e = [sum(map(int, x.split('+'))) for x in input().split('-')]
# print(e[0]-sum(e[1:]))
