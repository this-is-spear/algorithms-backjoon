answer = int(input())

for i in range(answer//4+1, answer+1):
    if i + sum(list(map(int, str(i)))) == answer:
        print(i)
        exit(0)
else:
    print(0)