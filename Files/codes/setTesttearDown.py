import unittest




class Testing(unittest.TestCase):
    def setUp(self) -> None:
        print("setting")

    def test_1(self):
        print("testing")
        self.assertEqual("kalyan".upper(),"KALYAN")
    @unittest.skipIf("kalyan".upper()=="Reddy",
                     "not equal")
    def test_2(self):
        print("testing")
        self.assertEqual("kalyan".upper(),"KALYAN")
    def tearDown(self) -> None:
        print("teared")
