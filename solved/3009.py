setX = []
setY = []
for _ in range(3):
    a,b = map(int,input().split())
    if a in setX:
        setX.remove(a)
    else:
        setX.append(a)
    if b in setY:
        setY.remove(b)
    else:
        setY.append(b)

print(setX[0], setY[0])