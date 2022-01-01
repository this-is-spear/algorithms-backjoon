for _ in range(int(input())):
    a = int(input())
    answer = 0
    k = 0
    for _ in range(a):
        b,c = map(float,input().split())
        answer += b*c
        k += b
    print(int(k), round(answer/k, 1))