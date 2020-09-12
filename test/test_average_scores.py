import unittest
import unittest.mock as mock
from format_output import average_scores

def test_average(self):
    with mock.patch('builtins.input', side_effect=[85,90,95]):
        assert average_scores.average() == 90

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

