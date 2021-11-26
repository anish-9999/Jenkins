#!/usr/bin/python3
# Test case for Fibonacci
import unittest

from Fib import Fibonacci

class Testfib(unittest.TestCase):
    def test_list_int(self):
        data=9
        result=Fibonacci(data)
        self.assertEqual(result,34)

if __name__ == '__main__':
    unittest.main()
