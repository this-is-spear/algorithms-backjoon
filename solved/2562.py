
# exec(9*"")
a, num = 0, 0
for i in range(9):
    print(i)
    b = int(input())
    if a < b:
        a = b
        num = i + 1

print(a)
print(num)