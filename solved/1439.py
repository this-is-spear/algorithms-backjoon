# 연속된 숫자들을 하나로 모은다.

a = input()
arr = []
for i in a:
    if arr:
        if arr[-1] != i:
            arr.append(i)
    else:
        arr.append(i)
print(min(arr.count('1'),arr.count('0')))
