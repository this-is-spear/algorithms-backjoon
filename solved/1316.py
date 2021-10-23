# 최적 코드
# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, aey=word.find):
#         result += 1
# print(result)

l = 0
for i in range(int(input())):
    sol_str = input()
    temp = ''
    while sol_str:
        if sol_str[0] == sol_str[1:2]:
            sol_str = sol_str[1:]
        else:
            temp += sol_str[0]
            sol_str = sol_str[1:]
    if len(temp) == len(set(temp)):
        l += 1
print(l)

# import unittest
# var = [['happy', 1], ['new', 1], ['year',1], ['aba', 0], ['abab', 0], ['a', 1]]  # test variable.... [[in, out], ...]
# class CustomTest(unittest.TestCase):
#     def test(self):
#         for a, b in var:
#             self.assertEqual(solution(a), b)
## Ran 1 test in 0.002s
# def solution(sol_str):
#     temp = ''
#     l = 0
#     while sol_str:
#         if sol_str[0] == sol_str[1:2]:
#             sol_str = sol_str[1:]
#         else:
#             temp += sol_str[0]
#             sol_str = sol_str[1:]
#     if len(temp) == len(set(temp)):
#         l += 1
#     return l
## 축약한다.
## 단어 중복이 존재하는지 확인한다.
## 맞는 개수를 리턴한다.
# if __name__ == '__main__':
#     unittest.main()
