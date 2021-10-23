# 전체적인 런타임 이유 str이 입력받지 못해서 런터임 에러가 떴다

# Ran 1 test in 0.014s
def solution(str_len):
    var = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in var:
        str_len = str_len.replace(i, '*')
    print(len(str_len))
    return len(str_len)

# runtime error - Ran 1 test in 0.003s
# 앞에 한자리 들고와서 비교
# 맞으면 세자리씩 비교
# 만약 맍는게 있다면 그만큼 삭제
# 틀리면 하나만 삭제
# l은 지운만큼 추가
# def solution(str):
#     var = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#     l = 0
#     while str:
#         l += 1
#         if str[0] in 'cdlnsz':
#             if str[0:2] in var:
#                 str = str[1:]
#             elif str[0:3] in var:
#                 str = str[2:]
#         str = str[1:]
#     print(l)
#     return l


# runtime error - Ran 1 test in 0.010s
# def solution(str):
#     var = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#     l = len(str)
#     for i in var:
#         if i in str:
#             l -= str.count(i)
#     print(l)
#     return l
import unittest


class CustomTest(unittest.TestCase):
    def test(self):
        for a, b in var2:
            try:
                self.assertEqual(solution(a), b)
            except assertionError:
                print(a)


var2 = [['c-evapc=ic-i', 9],

        ['cimcirastes=ams=are', 17],

        ['ljuljamsenanjihaljai', 16],

        ['dz=epariz=eparetud-epare', 20],

        ['abcc-c=dd-dz=efghijalljmnnjoprss=tuvzz=dzempersljjlljnjjnnjjdzz=d-z', 52],

        ['ljldz=j', 4],

        ['dz=dljz=', 4],

        ['ddz=z=', 3],

        ['nljj', 3],

        ['c=c=', 2],

        ['c=jc-jdz=jd-jljjnjjs=jz=joooooc=z=c-z=dz=z=d-z=ljz=njz=s=z=z', 36],

        # ['dadbdcdddedfdgdhdidjdadldmdndodpdrdsdtdudvdzoooodc=dc-ddz=dd-dljdnjdsz=dz=d', 65],

        ['dz=d-d-dz=dddz=z=s=z=z', 11],

        ['dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=dz=d', 34],

        ['z=z=dz=dz=ddz=ddz=dz=dz=z=z=', 12],

        ['nnlnlnllnnnnlnlnllnnnnlnlnllnnnnlnlnllnnnnlnlnllnnnnlnlnllnnjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 99]
        ]

if __name__ == '__main__':
    unittest.main()
