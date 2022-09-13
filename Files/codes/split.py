import unittest

class TestSplitMethod(unittest.TestCase):
    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(),['Python' , 'Testing'])
    def test_split_by_comma(self):
        actual='open,high,low,close'.split(',')
        out=['open','high','low','close']
        self.assertEqual(actual,out)
    def test_split_by_hash(self):
        actual='summer#time#vibes'.split('#')
        out=['summer','time','vibes']
        self.assertEqual(actual,out)