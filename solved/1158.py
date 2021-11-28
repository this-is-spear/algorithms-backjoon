from collections import deque

a, b = map(int, input().split())
deque = deque([i for i in range(1, a + 1)])
time = 0
answer = []
while deque:
    time += 1
    if time % b == 0:
        answer.append(deque.popleft())
    else:
        deque.append(deque.popleft())
print('<'+', '.join(str(i) for i in answer)+'>')