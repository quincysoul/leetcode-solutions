import unittest
from ...solutions._704_binary_search import Solution


class Test_search(unittest.TestCase):
    def test_expected(self):
        "Fast solution should return left most element=target's index."
        self.assertEqual(Solution.search(self, [0, 1, 2, 24, 24, 24, 25], 2), 2)

    def test_expected_when_number_dne(self):
        "Fast solution should return -1 when target does not exist in array."
        self.assertEqual(Solution.search(self, [0, 1, 2, 24, 24, 24, 25], 3), -1)


class Test_search_with_bisect_impl(unittest.TestCase):
    def test_expected(self):
        "Longer solution should return left most element=target's index."
        self.assertEqual(
            Solution.search_with_bisect_impl(self, [0, 2, 24, 24, 24, 25], 2), 1
        )

    def test_expected_when_number_dne(self):
        "Longer solution return -1 when target does not exist in array."
        self.assertEqual(
            Solution.search_with_bisect_impl(self, [0, 1, 2, 24, 24, 24, 25], 3), -1
        )

