import sys
a = [0 for _ in range(20)]
input()
for i in sys.stdin:
    if 'add' in i:
        a[int(i.split()[1])-1] = 1
    elif 'remove' in i:
        a[int(i.split()[1])-1] = 0
    elif 'check' in i:
        print(a[int(i.split()[1])-1])
    elif 'toggle' in i:
        a[int(i.split()[1])-1] = 1 if a[int(i.split()[1])-1] == 0 else 0
    elif 'all' in i:
        a = [1 for _ in range(20)]
    else:
        a = [0 for _ in range(20)]


#
# import sys
# a = set()
# input()
# for i in sys.stdin:
#     if 'add' in i:
#         a.add(int(i.split()[1]))
#     elif 'remove' in i:
#         a.remove(int(i.split()[1]))
#     elif 'check' in i:
#         if int(i.split()[1]) in a:
#             print('1')
#         else:
#             print('0')
#     elif 'toggle' in i:
#         if int(i.split()[1]) in a:
#             a.remove(int(i.split()[1]))
#         else:
#             a.add(int(i.split()[1]))
#     elif 'all' in i:
#         a = set(i for i in range(1, 21))
#     else:
#         a = set()
