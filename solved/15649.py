# 1. 모든 숫자 중에 하나를 선택한다.
# 2. 남은 숫자 중에 하나를 선택한다.
# 3. 끝까지 선택한다.
# 4. 이 과정을 모두 반복한다.

n, m = map(int, input().rsplit())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
