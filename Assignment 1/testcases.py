​import unittest
from A1 import *
​
class Testing(unittest.TestCase) :
    def test_add(self) :
        self.assertEqual(maxBlock("hoopla"), 2)
        self.assertEqual(maxBlock("abbCCCddBBBxx"), 3)
        self.assertEqual(maxBlock(""), 0)
        self.assertEqual(maxBlock("xyz"), 1)
        self.assertEqual(maxBlock("xxyz"), 2)
        self.assertEqual(maxBlock("abbbcbbbxbbbx"), 3)
        self.assertEqual(maxBlock("XXBBBbbxx"), 3)
        self.assertEqual(maxBlock("XXBBBBbbxx"), 4)
        self.assertEqual(maxBlock("XX2222BBBbbXX2222"), 4)
​
if __name__=="__main__" :
    unittest.main()