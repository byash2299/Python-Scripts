import unittest
import main

class testMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sdaf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

unittest.main()