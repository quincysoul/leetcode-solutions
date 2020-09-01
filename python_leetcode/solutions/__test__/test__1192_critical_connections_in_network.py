import unittest
from ...solutions._1192_critical_connections_in_network import Solution


class Test_search(unittest.TestCase):
    def node_extractor(self, connections):
        nodes = {}
        for el in connections:
            if nodes.get(el[0]):
                nodes[el[0]].append(el[1])
            else:
                nodes[el[0]] = [el[1]]
            if nodes.get(el[1]):
                nodes[el[1]].append(el[0])
            else:
                nodes[el[1]] = [el[0]]
        return nodes

    def test_expected(self):
        "Solution should return only the critical connections in the graph."
        solution = Solution()
        critical = [[1, 3]]
        list_res = solution.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
        expected = self.node_extractor(critical)
        actual = self.node_extractor(list_res)
        self.assertDictEqual(expected, actual)

