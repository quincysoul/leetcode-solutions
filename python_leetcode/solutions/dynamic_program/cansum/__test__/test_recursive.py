import unittest
from ...cansum.recursive import Solution


class Test(unittest.TestCase):
    def test_expected_alvins(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(True, solution.recursive_can_sum(7, [2, 3]))

    def test_expected_alvins_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(True, solution.recursive_can_sum(7, [5, 3, 4, 7]))

    def test_expected_alvins_3(self):
        "Should return False."
        solution = Solution()
        self.assertEqual(False, solution.recursive_can_sum(7, [2, 4]))

    def test_expected(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(True, solution.recursive_can_sum(10, [10]))

    def test_expected_1(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(True, solution.recursive_can_sum(10, [5, 5]))

    def test_expected_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(True, solution.recursive_can_sum(100, [90, 10]))

    # def test_expected_3(self):
    #     "Should return True if possible."
    #     solution = Solution()
    #     self.assertEqual(True, solution.recursive_can_sum(300, [7, 14]))

