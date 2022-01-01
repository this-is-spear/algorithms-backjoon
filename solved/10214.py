for _ in range(int(input())):
    arr = [0,0]
    for _ in range(9):
        a,b = map(int,input().split())
        arr[0] += a
        arr[1] += b
    else:
        if arr[0]>arr[1]:
            print("Yonsei")
        elif arr[0] < arr[1]:
            print("Korea")
        else:
            print("Draw")