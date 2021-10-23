import math
i = int(input())
print(math.sqrt(i).__int__() if math.sqrt(i).is_integer() else math.sqrt(i).__int__()+1)

#
# n=int(input())**0.5;print(int(n)+int(n%1>0))