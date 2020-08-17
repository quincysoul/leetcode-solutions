"""
Summary:
    Time Complexity: O(
        * 
    Space Complexity: O(
Trick:

Bibliography:

Args:
"""


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        # Desired data structure for nodes to be DFSed:
        # connections = [[0,1],[1,2],[2,0],[1,3]]
        # nodes = {
        # 0: {1,2}
        # 1: {0,2,3}
        # 2: {0,1}
        # 3: {1}
        # }
        nodes = {}

        for i in range(n):
            nodes[n] = {}
        for i in range(n):
            node = connections[n][0]
            connected_node = connections[n][1]

            nodes[node][connected_node] = 1
            nodes[connected_node][node] = 1

        dfs_stack = [0]
        while dfs_stack:
            dfs(dfs_stack.pop())

    def dfs(self, nodes, position):
        visited = {}
        non_critical = {}

        neighbors = nodes[position]
        for node in neighbors:
            if visited[node] == 1:
                non_critical[node] = 1
            dfs(node)