a = '472'
b = '385'

a = int(input())
b = a = input()
while b:
    print(a * int(b[-1]))
    b = b[:-1]
print(a*int(a))

