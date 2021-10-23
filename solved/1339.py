dic_num = {}
for _ in range(int(input())):
    a = input()
    for index, i in enumerate(a):
        try:
            dic_num[i] += 1 * 10**(len(a)-1-index)
        except:
            dic_num[i] = 1 * 10**(len(a)-1-index)
an = 0
num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(num_arr.pop()*i for i in sorted(dic_num.values(), reverse=True)))
