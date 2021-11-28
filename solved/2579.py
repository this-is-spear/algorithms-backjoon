# 최대값 출력
# 점화식으로 가능하지 않을까?

# 한칸 이동 두칸 이동

# 각 칸 이동하는 도중 그 전칸에서 가장 높은 값을 가지고 있자
# 첫 칸은 기본으로 저장하고
# 두 번째 칸은 첫 칸에서 저장
# 세 번째 칸은 첫 칸과 두 번째 칸의 값중 가장 큰 값에다 본인 인덱스 값 더해 저장
# 총 n 칸을 가는데
# 전에 1칸을 갔으면 다음은 한칸을 이용 못한다.

a = int(input())
dp = [0 for _ in range(a + 1)]
arr = [0]
for _ in range(a):
    arr.append(int(input()))
dp[1] = arr[1]
if len(dp) > 2:
    dp[2] = arr[1] + arr[2]
for i in range(3, a + 1):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i-1] + arr[i])
print(dp[a])

# 두 값을 저장해야하는 것인가?
# 한 칸 전의 값을 더한 값과 두 칸 전의 값을 더한 값
