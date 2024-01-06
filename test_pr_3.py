import unittest

def revers_1 (arr):
    arr.reverse()
    return arr


def revers_2 (arr):
    temp = []
    for i in range (len(arr)-1, -1, -1):
        temp.append(arr[i])
    return temp



class reversTestCase(unittest.TestCase):
    def test_1(self):
        res = revers_1([1, 43, 6, 22, 756])
        exp_res = [756, 22, 6, 43, 1]
        self.assertEqual(res, exp_res)

    def test_2(self):
        res = revers_2([1, 43, 6, 22, 756])
        exp_res = [756, 22, 6, 43, 1]
        self.assertEqual(res, exp_res)

