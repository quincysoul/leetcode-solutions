import unittest
from ...solutions._200_number_of_islands_dfs_slow import Solution


class Test_number_islands_dfs(unittest.TestCase):
    def test_expected(self):
        "Should return the number of islands determined by DFS valid nodes (only 1s, only up down left right)."
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 1)

    def test_expected_2(self):
        "Should return the number of islands determined by DFS valid nodes (only 1s, only up down left right)."
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "1", "0"],
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 2)

    def test_expected_3(self):
        "Should return the number of islands determined by DFS valid nodes (only 1s, only up down left right)."
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 3)

