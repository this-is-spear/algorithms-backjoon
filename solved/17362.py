# ?
# 1. 4씩 나눔 0줄 부터 시작
# 2. 짝수 줄이면 1부터 4까지 올려감
# 3. 홀수 줄이면 반대로 5부터 1씩 줄여나감
# 4. ㅇㅋ?
# 그냥 8의 배수마다 올리면 되는 것 아닌가?
# 1
# 1+8
# 1+16 ...
# (1000-1)//8.
a = int(input())
print((a-1)%8+1 if (a-1)%8+1 <= 5 else 9 - (a-1)%8)