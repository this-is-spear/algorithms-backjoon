a,b = map(int,input().split())
arr = []
# b까지 더한 수에 a까지 더한 수를 뺴자
def solv(solv_i):
    temp = 1
    i = 1
    answer = 0
    while solv_i >= temp:
        answer += i * i
        i += 1
        temp += i
    else:
        answer += (solv_i - temp + i) * i
    return answer
print(solv(b) - solv(a-1))
