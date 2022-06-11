a, b = input().split()


def find_max(str_val):
    str_val = list(str_val)
    for i in range(len(str_val)):
        str_val[i] = '6' if str_val[i] == '5' else str_val[i]
    return int(''.join(str_val))


def find_min(str_val):
    str_val = list(str_val)
    for i in range(len(str_val)):
        str_val[i] = '5' if str_val[i] == '6' else str_val[i]
    return int(''.join(str_val))


max_val = find_max(a) + find_max(b)
min_val = find_min(a) + find_min(b)
print(min_val, max_val)
