while True:
    a = input()
    if a == '.':
        break
    stack = []
    for i in a:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
