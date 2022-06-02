
# string = ''

# 값을 받는다.
# 원래 저장되어 있는 값과 비교한다.
# ( 다음으로 ( 가 오는 상황에서는 스택에 1 값을 추가한다.
# ( 다음으로 ) 가 오는 상황에서는 스택 - 1 만큼 결과값에 추가한다.
# ) 다음으로 ) 가 오는 상황에서는 스택에서 1을 뺴고, 결과값에 1을 추가한다.
# ) 다음으로 ( 가 오는 상황에서는 아무일이 일어나지 않는다.


string = input()
current_index = string[0]
result = 0
stack = 1

for i in string[1:]:
    if current_index == '(' and i == '(':
        stack += 1
    elif current_index == '(' and i == ')':
        result += stack - 1
    elif current_index == ')' and i == ')':
        stack -= 1
        result += 1
    current_index = i

print(result)
