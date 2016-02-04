from functools import reduce
import unittest


def f_fact(n):
    if n>1:
        return reduce(lambda x,y: x*y, range(1,n+1))
    elif n == 0:
        return 1
    else:
        return print('Bad Input')

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(f_fact(5), 120)
        self.assertEqual(f_fact(0), 1)
        self.assertEqual(f_fact(-5), None)

if __name__ == '__main__':
    unittest.main()