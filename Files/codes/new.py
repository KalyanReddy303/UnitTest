import unittest

class WidgetTestCase(unittest.TestCase):


   def test_(self):
       self.assertTupleEqual((1,2,3),(1,2,3))
if __name__=="__main__":
    unittest.main()