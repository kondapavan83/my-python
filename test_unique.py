import unittest
import unique
class testunq(unittest.TestCase):
    def testunq(self):
        l=['a','b','c','a','c','d','r','d','b','a','b','c','a','b']
        result = unique.unq(l)
        self.assertEqual(result,{'b', 'a', 'r', 'c', 'd'})
    def testnum(self):
        list=['1','2','3','3']
        result2 = unique.unq(list)
        self.assertEqual(result2,{'1','2','3'})
if __name__=='__main__':
    unittest.main()
