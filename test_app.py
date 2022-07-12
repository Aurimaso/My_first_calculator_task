import unittest
from app import calc_eval

class Testapp(unittest.TestCase):
    def test_app(self):
        self.assertEqual(2, calc_eval('10/5'))
        self.assertEqual(1.25, calc_eval('2.5/2'))
        self.assertEqual(-12, calc_eval('-2*6'))
        self.assertEqual('No devision from zero', calc_eval('10/0'))
        self.assertEqual('Please try again :(', calc_eval('ad/2'))
        
        