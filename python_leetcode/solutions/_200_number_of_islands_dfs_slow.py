from typing import List

"""
Time Complexity: O(M*N) (close to N^2)
Space Complexity: O(M*N) (close to N^2)
While this solution is easier to write it is extremely sub-optimal on Space Complexity
Due to the use of recursion. Therefore, it must be switched to BFS solution for best answer.

Because we have seen they want number of islands, we can use Depth First Search, and stop searching further
any time a 0 is hit, that is water.

dfs typically takes: currentNode, visitedNodes, graph - we dont care about lookign at visited nodes in DFS.

How should visited nodes look??
{
    0: { 0: True, },
    1: {},
    2: {},
    ...
}
or it could look like
{
    "0,0":True,
    "0,1":True,
    ...
}
The second one is cleaner looking to me.

        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]


"""


class Solution:
    def __init__(self):
        self.countIslands = 0
        self.visited = {}

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                position = f"[{i},{j}]"
                if self.visited.get(position):
                    continue
                elif grid[i][j] == "0":
                    self.visited[position] = True
                    continue
                elif grid[i][j] == "1":
                    self.countIslands += 1
                    self.dfs([i, j], grid)
        return self.countIslands

    def dfs(self, current, grid):
        #               up      down    left    right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            i = current[0] + direction[0]  # y
            j = current[1] + direction[1]  # x
            if i > -1 and i < len(grid) and j > -1 and j < len(grid[0]):
                position = f"[{i},{j}]"
                if self.visited.get(position):
                    continue
                else:
                    self.visited[position] = True
                    # if valid node detected to continue dfs...
                    if grid[i][j] == "1":
                        self.dfs([i, j], grid)

