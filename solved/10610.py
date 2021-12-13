a = input()
if sum(int(i) for i in a) % 3 or '0' not in a:
    print(-1)
else:
    print(''.join(i for i in sorted(list(a), reverse=True)))