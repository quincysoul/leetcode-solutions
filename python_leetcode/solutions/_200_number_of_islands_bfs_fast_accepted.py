from typing import List

import collections

"""
Time Complexity: O(M*N) 
    (close to N^2)(OPTIMAL)
Space Complexity: O( min(m,n) ) 
    (OPTIMAL)

-----------
The concept of BFS.
-----------
In DFS, we see a valid node.next, and we go to it. Then we call DFS on it immediately (recursive).

In BFS, we see a valid node.next, we go and add it to the queue. It is from there that we can call BFS on each queued item
It is breadth, not depth, we do not go deep, we just look to node.next(s) and look at those. Then go from there in que.
"""


class Solution:
    def __init__(self):
        self.countIslands = 0
        self.visited = {}
        self.q = collections.deque()

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                position = [i, j]

                if self.visited.get(f"{position}"):
                    continue
                elif grid[i][j] == "0":
                    self.visited[f"{position}"] = True
                    continue
                elif grid[i][j] == "1":
                    self.countIslands += 1
                    self.visited[f"{position}"] = True
                    self.bfs(position, grid)
        return self.countIslands

    def bfs(self, current, grid):
        # up down left right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for direction in directions:
            i = current[0] + direction[0]
            j = current[1] + direction[1]
            position = [i, j]
            # print(f"bfs({position},{grid})")
            if i > -1 and j > -1 and i < len(grid) and j < len(grid[0]):
                if self.visited.get(f"{position}"):
                    continue
                elif grid[i][j] == "0":
                    self.visited[f"{position}"] = True
                    continue
                elif grid[i][j] == "1":
                    self.visited[f"{position}"] = True
                    self.q.appendleft(position)

        while len(self.q) > 0:
            self.bfs(self.q.pop(), grid)


"""
With grid = [[1 0 1 0 1]
             [1 1 0 1 1]
             [1 0 1 0 1]
We enter bfs at [0,0].
We examine up is invalid.
We examine down is valid [1,0]
    We examine it is 1, so a valid node.
        We add this node to the queue: q:[ [1,0], ]
We examine left is invalid.
We examine right is valid.
    We examine it is 0, so we just mark as visited and dont add.
We check the queue. q:[ [1,0], ]. BFS the q top element. self.bfs([1,0],grid)
-
We enter bfs at [1,0]
We examine up is visited, and *continue*.
We examine down is valid [2,0] and add to queue: q:[ [2,0], ]
We examine left is invalid.
We examine right is valid: [1,1] and add to queue: q:[ [2,0], [1,1]]
We check the q:[ [2,0], [1,1]] BFS the q top element. self.bfs([2,0],grid)
-
We enter bfs at [2,0]
We examine up is visited, and *continue*.
We examine down is invalid, and *continue*.
We examine left is invalid.
We examine right is valid.
    It is a 0. We mark as visited.
    We continue.
We check the q:[ [1,1]]  BFS the q top element. self.bfs([1,1],grid)
-
We enter bfs at [1,1].
Everything was visited or a 0. The 0s are marked as visited.
q is empty, so we contiue through our loop skipping all visited nodes. We hit [0,2] and perform BFS.
"""
