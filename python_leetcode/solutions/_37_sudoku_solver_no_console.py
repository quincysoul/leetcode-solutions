from typing import List
import math


class Solution:
    def __init__(self):
        self.len_board = 9
        self.unsolved = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.unsolved = self.find_unsolved(board)

        i = 0
        while i < len(self.unsolved):
            position = self.unsolved[i]
            current_value = self.quick_get(board, *position)
            self.quick_set(board, *position, current_value + 1)
            if self.quick_get(board, *position) == 10:
                self.quick_set(board, *position, 0)
                i -= 1
            elif self.is_valid(board, *position):
                i += 1
                continue
        return board

    def is_valid(self, board, i, j):
        element = self.quick_get(board, i, j)

        for col in range(self.len_board):
            if col != j and element == self.quick_get(board, i, col):
                return False

        for row in range(self.len_board):
            if row != i and element == self.quick_get(board, row, j):
                return False

        bI = i // 3
        bJ = j // 3
        sI = bI * 3
        sJ = bJ * 3

        for h in range(3):
            for w in range(3):
                if (
                    sI + h != i
                    and sJ + w != j
                    and self.quick_get(board, sI + h, sJ + w) == element
                ):
                    return False
        return True

    def quick_set(self, board, i, j, val):
        board[i][j] = str(val)

    def quick_get(self, board, i, j):
        return int(board[i][j])

    def find_unsolved(self, board):
        unsolved = []
        for i in range(self.len_board):
            for j in range(self.len_board):
                if board[i][j] == "." or board[i][j] == " " or board[i][j] == "":
                    board[i][j] = "0"
                    unsolved.append([i, j])
        return unsolved
