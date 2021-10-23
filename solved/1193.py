# sum 2 1개  순번 1
# sum 3 2개  순번 2 ~ 3
# sum 4 3개  순번 4 ~ 6
# sum 5 4개  순번 7 ~ 10
# sum 6 5개  순번 11 ~ 15...

a = int(input())
a, i = 1, 1
while i < a:
    a += 1
    i += a
print("{0}/{1}".format(i - a + 1, a + 1 - (i - a + 1)) if a % 2 else "{0}/{1}".format(a + 1 - (i - a + 1), i - a + 1))
