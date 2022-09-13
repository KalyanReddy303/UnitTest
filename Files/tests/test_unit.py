import unittest


def Student(name):
    return name


class Test_student(unittest.TestCase):
    def test_name(self):
        self.assertEqual(Student("kalyan"), "kalyan")
        with self.assertRaises(AssertionError) as E:
            print(E)

