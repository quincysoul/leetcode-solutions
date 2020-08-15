import unittest
from ...solutions._37_sudoku_solver import Solution


class Test_sudoku_solver(unittest.TestCase):
    def test_expected(self):
        "Solver should return a solved sudoku board."
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        input = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]

        solution = Solution()
        self.assertEqual(expected, solution.solveSudoku(input))

    # def test_backtracking_slow(self):
    #     "Solver should return a solved sudoku board."
    #     expected = [
    #         ["9", "8", "7", "6", "5", "4", "3", "2", "1"],
    #         ["2", "4", "6", "1", "7", "3", "9", "8", "5"],
    #         ["3", "5", "1", "9", "2", "8", "7", "4", "6"],
    #         ["1", "2", "8", "5", "3", "7", "6", "9", "4"],
    #         ["6", "3", "4", "8", "9", "2", "1", "5", "7"],
    #         ["7", "9", "5", "4", "6", "1", "8", "3", "2"],
    #         ["5", "1", "9", "2", "8", "6", "4", "7", "3"],
    #         ["4", "7", "2", "3", "1", "9", "5", "6", "8"],
    #         ["8", "6", "3", "7", "4", "5", "2", "1", "9"],
    #     ]
    #     input = [
    #         [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         [".", ".", ".", ".", ".", "3", ".", "8", "5"],
    #         [".", ".", "1", ".", "2", ".", ".", ".", "."],
    #         [".", ".", ".", "5", ".", "7", ".", ".", "."],
    #         [".", ".", "4", ".", ".", ".", "1", ".", "."],
    #         [".", "9", ".", ".", ".", ".", ".", ".", "."],
    #         ["5", ".", ".", ".", ".", ".", ".", "7", "3"],
    #         [".", ".", "2", ".", "1", ".", ".", ".", "."],
    #         [".", ".", ".", ".", "4", ".", ".", ".", "9"],
    #     ]

    #     solution = Solution()
    #     self.assertEqual(expected, solution.solveSudoku(input))
