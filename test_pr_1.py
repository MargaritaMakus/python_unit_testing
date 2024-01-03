def minimal(l):
    min_num = l[0]
    for el in l:
        if el < min_num:
            min_num = el 
    return (min_num)

nums1 = [5,4,9,8]
# minimal(nums1)


import unittest

class minTestCase(unittest.TestCase):
    def test_1(self):
        res = minimal([7,44,6,23,43,9])
        expectet_res = 6
        self.assertEqual(res, expectet_res)

    def test_2(self):
        res = minimal([-9, -3, -8, -2, -11])
        expectet_res = -11
        self.assertEqual(res, expectet_res)
