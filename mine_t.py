from mine import Mine
import unittest
from vec import Vec

class MineTest(unittest.TestCase):
    def test_workswithhash(self):
        self.assertEqual(Mine(Vec(3,3),controlled=True), Mine(Vec(3,3),controlled=True))
        self.assertNotEqual(Mine(Vec(3,3),controlled=False), Mine(Vec(3,3),controlled=True))
        
    def test_workswithset(self):
        s = set()
        s.add(Mine(Vec(3,3), controlled=True))
        self.assertEqual(1,len(s))
        s.remove(Mine(Vec(3,3),controlled=True))
        self.assertEqual(0,len(s))

