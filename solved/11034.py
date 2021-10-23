while True:
    try:
        a, b, c = map(int, input().split())
        an = 0
        print(max(b-a-1, c-b-1))
    except:
        break

