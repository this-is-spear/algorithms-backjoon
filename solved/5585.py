n = 1000 - int(input())
a = [1, 5, 10, 50, 100, 500]
an = 0
while n > 0:
    a_pop = a.pop()
    an += n//a_pop
    n %= a_pop
print(an)
