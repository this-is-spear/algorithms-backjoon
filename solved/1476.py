a, b, c = map(int, input().split())
k = 1
time = 0
temp_a, temp_b, temp_c = 0,0,0
while True:
    time += 1
    temp_a = temp_a % 15 + 1
    temp_b = temp_b % 28+ 1
    temp_c = temp_c % 19 + 1
    if temp_a == a and temp_b == b and temp_c == c:
        break
print(time)