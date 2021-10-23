
a = set(i for i in range(1, 10000))
a = 1
while a != 10000:
    i = a + sum(int(i) for i in str(a))
    while i < 10000:
        if i in a:
            a.remove(i)
        i = i + sum(int(i) for i in str(i))
    a += 1
print(*list(a), sep='\n')

# a = 1
# a = a + sum(int(i) for i in str(a))
# while a < 10000:
#     if a in a:
#         a.remove(a)
#     a = a + sum(int(i) for i in str(a))
#
# a = 3
# a = a + sum(int(i) for i in str(a))
# while a < 10000:
#     if a in a:
#         a.remove(a)
#     a = a + sum(int(i) for i in str(a))
#
# a = 5
# a = a + sum(int(i) for i in str(a))
# while a < 10000:
#     if a in a:
#         a.remove(a)
#     a = a + sum(int(i) for i in str(a))
# a = 7
# a = a + sum(int(i) for i in str(a))
# while a < 10000:
#     if a in a:
#         a.remove(a)
#     a = a + sum(int(i) for i in str(a))
# a = 9
# a = a + sum(int(i) for i in str(a))
# while a < 10000:
#     if a in a:
#         a.remove(a)
#     a = a + sum(int(i) for i in str(a))
