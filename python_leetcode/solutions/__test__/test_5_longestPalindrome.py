import unittest
from ...solutions._5_longest_palindrome import Solution


class Test_find_longest_palindrome(unittest.TestCase):
    def test_expected(self):
        "Should return longest palindrome in string."
        self.assertIn(Solution.longestPalindrome(self, "babad"), ["bab", "aba"])
