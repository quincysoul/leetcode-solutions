from typing import List
import math

"""
Summary:

Trick:
    A few options:
    1. Backtracking
    2. DFS
    - And, ds options of stack, deque, or system stack via recurse.
    The brute force is to try every possible number combination, O(9^N)
    This question is known to be asked in phone interviews.

Bibliography:
    Solution source: techwithtim:
    https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

Args:
    board (List[List]): 2d array of a valid sudoku board, as below.
    example_board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
"""


class Solution:
    def __init__(self):
        self.len_board = 9
        self.stack = []
        self.solved = {}
        self.n = 1
        self.n_expected = "Unknown O(N)"

    # Now we know if any given element is valid, we can look at all the elements
    # and try different values if not valid
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.len_board = len(board)
        self.n_expected = (math.factorial(self.len_board)) ** self.len_board

        self.solved = self.get_pre_solved(board)

        for i in range(self.len_board):
            for j in range(self.len_board):
                self.n += 1
                self.print_n()
                self.pretty_print(board, i, j)

                element = board[i][j]

                if self.solved.get(f"[{i}][{j}]"):
                    continue
                elif board[i][j] == "." or board[i][j] == "0":
                    board[i][j] = "0"
                    if self.solve(board, i, j) == True:
                        continue
        while self.stack:
            next_position = self.stack.pop()
            print(f"Changing to solve next_position: {next_position}")
            if board[next_position[0]][next_position[1]] == "0":
                self.solve(board, *next_position)
                self.pretty_print(board, *next_position)
        return board

    def solve(self, board, i, j):
        while (int(board[i][j])) < 10:
            board[i][j] = str(((int(board[i][j])) + 1))
            if board[i][j] == "10":
                board[i][j] = "0"
                self.pretty_print(board, i, j)
                next_position = self.stack.pop()
                print(f"Changing to solve next_position: {next_position}")
                self.solve(board, *next_position)
            if self.is_valid(board, i, j):
                self.stack.append([i, j])
                return True

    def is_valid(self, board, i, j):
        element = board[i][j]

        print(f"Comparing element... {element}")

        # Row valid element?
        for k in range(self.len_board):
            if board[i][k] == board[i][j] and k != j:
                return False
        # Col valid element?
        for k in range(self.len_board):
            if board[k][j] == board[i][j] and k != i:
                return False
        # 3x3 box valid element?
        """
        [0,0] [0,1] [0,2]
        [1,0] [1,1] [1,2]
        [2,0] [2,1] [2,2]
        """
        boxI = i // 3
        boxJ = j // 3
        startI = boxI * 3
        startJ = boxJ * 3
        for k in range(3):
            for l in range(3):
                if (
                    startI + k != i
                    and startJ + l != j
                    and board[startI + k][startJ + l] == element
                ):
                    return False
        return True

    def get_pre_solved(self, board):
        solved = {}
        for i in range(self.len_board):
            for j in range(self.len_board):
                element = board[i][j]
                if element != ".":
                    element = board[i][j]
                    position_str = f"[{i}][{j}]"
                    solved[position_str] = True
        return solved

    def print_n(self):
        print(f"O(N): {self.n}/{self.n_expected}")

    def pretty_print(self, board, i, j):
        for h in range(self.len_board):
            for w in range(self.len_board):
                if h == i and w == j:
                    print(f"[{board[i][j]}]", end="")
                else:
                    print(f" {board[h][w]} ", end="")
                if w == 8:
                    print("")
