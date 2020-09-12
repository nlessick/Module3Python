import unittest


class OperatorsTest(unittest.TestCase):
    def Test_equal(self):
        a = 7
        b = -2
        self.assertFalse(a == b)

    def test_notequal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a != b)

    def test_greaterthan_operator(self):
        a = 7
        b = -2
        self.assertFalse(a > b)

    def test_lessthan_operator(self):
        a = 7
        b = -2
        self.assertFalse(a < b)

    def test_greaterequal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a >= b)

    def test_lessequal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a <= b)


if __name__ == '__main__':
    unittest.main()
