for i in range(int(input())):
    a, _, c = map(int, input().split())
    a, t = divmod(c - 1, a)
    print("{0}{1:0>2}".format(t + 1, a + 1))

# def solution(a, b, c):
#     a, t = divmod(c-1, a)
#     print("{0}{1:0>2}".format(t+1, a + 1))
#     # print("{0}{1:0>2}".format(t, a + 1) if not t == 0 else "{0}{1:0>2}".format(1, a))
#
#
# if __name__ == '__main__':
#     # 나눠 떨어질 때 오류가 생긴다
#     solution(1, 2, 1)   # 오류
#     solution(1, 2, 2)   # 오류
#     solution(2, 1, 1)
#     solution(2, 1, 2)   # 오류
#     solution(6, 2, 6)   # 오류
#     solution(6, 2, 10)
#     solution(6, 2, 11)
#     solution(6, 2, 12)  # 오류
#     solution(6, 2, 3)
#     solution(6, 12, 7)
#     solution(6, 12, 10)
#     solution(30, 50, 72)
#     solution(30, 50, 698)
#     solution(30, 50, 699)
#     solution(30, 50, 700)

# from unittest import moca
# from nose.tools import *
# def test_moca():
#     orginal_input = moca.builtins.input
#     moca.builtins.input = lambda _: '2\n6 12 10\n30 50 72'  # 'entered value'
#     assert_equal(solution(), '4021203')
#     moca.builtins.input = orginal_input
