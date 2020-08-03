from typing import List


class Solution:
    visited = {}
    count = 0
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # top  # left  # right  # bottom

    def dfs(self, i, j, directions, grid):
        for direction in directions:
            currentI = i + direction[0]
            currentJ = j + direction[1]
            print(f"At [{currentI},{currentJ}]")
            # such that from [0,0] checking TOP at [-1,0], cI = -1, cJ = 0.
            if (
                currentI >= 0
                and currentI < len(grid)
                and currentJ >= 0
                and currentJ < len(grid[0])
            ):
                if self.visited.get(currentI).get(currentJ) == True:
                    print(f"it is true at [{currentI},{currentJ}]")
                    continue
                else:
                    self.visited[currentI][currentJ] = True
                    print(f"SET {currentJ} at {self.visited[currentI]}")
                    if grid[currentI][currentJ] == "1":
                        print(f"inner dfs call at cI: {currentI} cJ: {currentJ}")
                        self.dfs(currentI, currentJ, directions, grid)
            else:
                print("array index out of bounds. skipped")

            print(self.visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            self.visited[i] = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.visited.get(i).get(j) == True:
                    continue
                elif grid[i][j] == "0":
                    self.visited[i][j] = True
                    continue
                elif grid[i][j] == "1":
                    self.count += 1
                    print(f"initial dfs call at count: {self.count} at [{i},{j}]---")
                    self.visited[i][j] = True
                    self.dfs(i, j, self.directions, grid)
        print(f"the self.count is: {self.count}")
        return self.count


solution = Solution()
solution.numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
)

