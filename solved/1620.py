import sys
input = sys.stdin.readline
a, b = map(int, input().split())
name = []
arr_name = {}
for i in range(a):
    k = input().rstrip()
    arr_name[k] = i+1
    name.append(k)
for _ in range(b):
    quest = input().rstrip()
    if quest.isdigit():
        print(name[int(quest)-1])
    else:
        print(arr_name[quest])
