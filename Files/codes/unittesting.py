import unittest
def calculate(a,b):
    return a+b*a-b+a
class Test_Calculate(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(calculate(3,4),14)

