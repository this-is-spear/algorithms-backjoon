a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(list(input()))

visited = [[0]*b for i in range(a)]
answer = 0
for i in range(a):
    for k in range(b):
        if visited[i][k] == 0:
            visited[i][k] = 1
            answer += 1
            temp = k
            while arr[i][temp] == '-' and temp+1 < b:
                if arr[i][temp+1] == '-':
                    visited[i][temp+1] = 1
                    temp += 1
                else:
                    break
            temp = i
            while arr[temp][k] == '|' and temp+1 < a:
                if arr[temp + 1][k] == '|':
                    visited[temp+1][k] = 1
                    temp += 1
                else:
                    break
        else:
            pass
print(answer)
