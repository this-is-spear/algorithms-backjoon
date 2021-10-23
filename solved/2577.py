import math
a=1
exec(3*"a*=int(input());")
print([i for i in str(a)])
for i in range(10):
    print([a for a in str(a)].count(str(i)))
