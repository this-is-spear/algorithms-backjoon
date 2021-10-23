import unittest

var = [[0, 0], [1, 1]]  # test variable.... [[in, out], ...]


class CustomTest(unittest.TestCase):
    def test(self):
        for a, b in var:
            self.assertEqual(solution(a), b)


def solution(in_str):
    print()


if __name__ == '__main__':
    unittest.main()
