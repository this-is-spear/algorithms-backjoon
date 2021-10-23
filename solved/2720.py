for _ in range(int(input())):
    a = int(input())
    k = [1, 5, 10, 25]
    an = []
    while k:
        k_pop = k.pop()
        an.append(str(a//k_pop))
        a %= k_pop
    print(' '.join(an))