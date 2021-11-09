a = int(input())
ai = '666'
count = 0
int_i = 666
arr = []
while count <= 10000:
    if str(int_i).__contains__(ai):
        count += 1
        arr.append(int_i)
        if a == count:
            print(int_i)
            break
    int_i +=1