hamb = 2000
for i in range(3):
    k = int(input())
    if k < hamb:
        hamb = k
bev = 2000
for i in range(2):
    k = int(input())
    if k < bev:
        bev = k
print(hamb + bev - 50)