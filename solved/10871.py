b = list(map(int, input().split()))[1]
answer = []
for i in list(map(int, input().split())):
    if i < b:
        answer.append(str(i))
print(" ".join(answer))

# n,x,*a=map(int,open(0).read().split())
# for i in a:i<x!=print(i)
#
# a,b = map(int,input().split())
# score = [x for x in input().split() if int(x)<b]
# print(' '.join(score))