def bcs(a, b):
    while a!= 0 and b!= 0:
        if a>b:
            a%=b
        else:
            b%=a
    return(a+b)

# print(bcs(-15, -5))

import unittest

class bcsTestCase(unittest.TestCase):
    def test_1(self):
        res = bcs(15, 5)
        expectet_res = 5
        self.assertEqual(res, expectet_res)

    def test_2(self):
        res = bcs(64, 24)
        expectet_res = 8
        self.assertEqual(res, expectet_res)
