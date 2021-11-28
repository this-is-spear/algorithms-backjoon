from collections import deque
a = int(input())
arr = []
blue = 0
white = 0
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]
deque = deque([arr])
for _ in range(a):
    arr.append(list(map(int,input().split())))
while deque:
    item = deque.popleft()
    if sum([sum(i) for i in item]) == len(item[0]) ** 2:
        blue += 1
    elif sum([sum(i) for i in item]) == 0:
        white += 1
    else:
        for i in range(4):
            temp = []
            for k in item[dx[i]*(len(item[0])//2):dx[i]*(len(item[0])//2)+len(item[0])//2]:
                temp.append(k[dy[i]*len(item[0])//2:dy[i]*len(item[0])//2+len(item[0])//2])
            deque.append(temp)
        pass

print(white)
print(blue)