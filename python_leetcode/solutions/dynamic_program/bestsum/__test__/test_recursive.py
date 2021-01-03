import unittest
from ...bestsum.recursive import Solution


class Test(unittest.TestCase):
    def test_expected_alvins(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([7], solution.recursive_bestsum(7, [5, 3, 4, 7]))

    def test_expected_alvins_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([7], solution.recursive_bestsum(7, [5, 3, 4, 7]))

    def test_expected_alvins_3(self):
        "Should return False."
        solution = Solution()
        self.assertEqual(None, solution.recursive_bestsum(7, [2, 4]))

    def test_expected(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([10], solution.recursive_bestsum(10, [10]))

    def test_expected_1(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([5, 5], solution.recursive_bestsum(10, [5, 5]))

    def test_expected_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(
            [10, 90], solution.recursive_bestsum(100, [10, 90]),
        )

    # def test_expected_3(self):
    #     "Should return None if possible."
    #     solution = Solution()
    #     self.assertEqual(True, solution.recursive_bestsum(300, [7, 14]))

