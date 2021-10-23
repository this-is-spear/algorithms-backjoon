
num = input()
if int(num) < 10:
    num = num + '0'
new_num = num
time = 0
while True:
    time += 1
    first = int(new_num[0])+int(new_num[1])
    new_num = new_num[-1] + str(first)[-1]
    if new_num == num:
        print(time)
        breaa




