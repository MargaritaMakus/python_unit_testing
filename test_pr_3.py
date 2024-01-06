import pr3 as r
import unittest

class reversTestCase(unittest.TestCase):
    def test_1(self):
        res = r.revers_1([1, 43, 6, 22, 756])
        exp_res = [756, 22, 6, 43, 1]
        self.assertEqual(res, exp_res)

    def test_2(self):
        res = r.revers_2([1, 43, 6, 22, 756])
        exp_res = [756, 22, 6, 43, 1]
        self.assertEqual(res, exp_res)
