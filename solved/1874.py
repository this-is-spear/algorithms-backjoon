# k = int(input())
# arr_i = []
# for _ in range(k):
#     arr_i.append(int(input()))
# answer = ''
# arr = []
# i = 0
# while i <= k:
#     if arr:
#         if arr_i[0] == arr[-1]:
#             arr.pop()
#             arr_i.pop(0)
#             answer += '-'
#         else:
#             i += 1
#             arr.append(i)
#             answer += '+'
#     else:
#         i += 1
#         arr.append(i)
#         answer += '+'
# if len(arr_i) == 0:
#     print('\n'.join(i for i in answer[:-1]))
# else:
#     print('NO')
