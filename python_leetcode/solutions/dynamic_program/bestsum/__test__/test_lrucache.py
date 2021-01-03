import unittest
from ...howsum.lrucache import Solution


class Test(unittest.TestCase):
    # def test_expected_alvins(self):
    #     "Should return True if possible."
    #     solution = Solution()
    #     self.assertEqual([4, 3], solution.lru_cache_howsum(7, [5, 3, 4, 7]))

    # def test_expected_alvins_2(self):
    #     "Should return True if possible."
    #     solution = Solution()
    #     self.assertEqual([4, 3], solution.lru_cache_howsum(7, [5, 3, 4, 7]))

    # def test_expected_alvins_3(self):
    #     "Should return False."
    #     solution = Solution()
    #     self.assertEqual(None, solution.lru_cache_howsum(7, [2, 4]))

    # def test_expected(self):
    #     "Should return True if possible."
    #     solution = Solution()
    #     self.assertEqual([10], solution.lru_cache_howsum(10, [10]))

    def test_expected_1(self):
        "Should return [5, 5] if possible."
        solution = Solution()
        self.assertEqual([5, 5], solution.lru_cache_howsum(10, (5, 5)))

    def test_expected_2(self):
        "Should return 10 * 10 array if possible."
        solution = Solution()
        self.assertEqual(
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            solution.lru_cache_howsum(100, (10, 90)),
        )

    def test_expected_3(self):
        "Should return None when not possible."
        solution = Solution()
        self.assertEqual(None, solution.lru_cache_howsum(300, (7, 14)))

