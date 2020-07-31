import unittest
from python_leetcode.solutions._x_hello_world import hello_world


class Test_hello_world(unittest.TestCase):
    def test_expected(self):
        'helloWorld() prints "Hello World"'
        self.assertEqual(hello_world(), "Hello World")

    def test_not_expected(self):
        'helloWorld() prints "Hello World" NOT "fail this test please."'
        self.assertNotEqual(hello_world(), "fail this test please.")

