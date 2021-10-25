_ = int(input())
arr = list(map(int, input().split()))
a_a = [0, 1, 2]
index = 0
answer = 0
while arr:
    arr_pop = arr.pop(0)
    if a_a[index%3] == arr_pop:
        answer += 1
        index += 1
print(answer)