from typing import List

"""
Summary:
    Time Complexity: 
    Space Complexity: 
Trick:

Bibliography:https://github.com/zengtian006/LeetCode

Args:

"""


class Solution:
    def __init__(self):
        self.graph = {}
        self.rank = []
        self.low = []
        self.res = []

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        visited = {}
        for i in range(n):
            self.graph[i] = []
            self.rank.append(0)
            self.low.append(0)
            visited[i] = False

        self.fill_graph(connections)

        dfs_stack = [[0, None, 0, visited]]
        rank = 0
        while dfs_stack:
            item = dfs_stack.pop()
            current = item[0]
            parent = item[1]
            index = item[2]
            visited = item[3]
            self.rank[current] = index
            self.low[current] = index
            visited[current] = True

            nexts = self.graph[current]
            for next in nexts:
                if next == parent:
                    continue
                if visited[next] == False:
                    dfs_stack.append([next, current, index + 1, visited])
                    self.low[current] = min(self.low[current], self.low[next])
                elif visited[next] == True:
                    self.low[current] = min(self.low[current], self.low[next])

            if self.low[next] > self.rank[current]:
                self.res.append([next, current])

        print("Exited dfs_stack")
        print(self.res)
        return self.res

    def fill_graph(self, connections):
        for pair in connections:
            node = pair[0]
            connected = pair[1]
            self.graph[node].append(connected)
            self.graph[connected].append(node)
