# 1칸 1개
# 2칸 6개     2 ~ 7
# 3칸 12개    8 ~ 19
# 4칸 18개    20 ~ 37
# 5칸 24개    38 ~ 61

a = int(input())
i, a = 1, 0
while i < a:
    a += 1
    i += a * 6
else:
    print(a + 1)
