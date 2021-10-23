arr = []
for _ in range(int(input())):
    arr.append(int(input()))
answer, a_one = 0, arr.pop(0)
if len(arr) != 0:
    while True:
        if a_one > max(arr):
            break
        else:
            arr[arr.index(max(arr))] -= 1
            a_one += 1
            answer += 1
    print(answer)
else:
    print(0)
