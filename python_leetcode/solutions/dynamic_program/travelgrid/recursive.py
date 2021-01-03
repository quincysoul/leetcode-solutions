"""[summary]
Problem: m * n grid, and you can only go left or right once per turn
return the total possible number of turns to get to the bottom right.

Time Complexity: [O(2 ** n)]
    1. 
Space Complexity: [O(N)]
    * 
Returns:
    int: fibonacci number at n.
"""


class Solution:
    def recursive_grid_traveler(self, m, n) -> int:
        """
        Return the number of total possible turns.
        """

        if m == 1 or n == 1:
            return 1

        if m == 2 and n == 2:
            return 2

        if m == 2 and n > 2:
            return n
        if m > 2 and m == 2:
            return m

        return self.recursive_grid_traveler(m - 1, n) + self.recursive_grid_traveler(
            m, n - 1
        )


solution = Solution()

print(solution.recursive_grid_traveler(1, 1), "Expected:1")
print(solution.recursive_grid_traveler(2, 2), "Expected:2")
print(solution.recursive_grid_traveler(2, 3), "Expected:2")
print(solution.recursive_grid_traveler(3, 3), "Expected:6")
print(solution.recursive_grid_traveler(3, 4), "Expected:6")
print(
    solution.recursive_grid_traveler(200, 200),
    "Expected:25802631612885822800244581533935335026869906110545776499962170319780283802669663809106916170169547105655150024437788000",
)
print(
    solution.recursive_grid_traveler(200, 200),
    "Expected:25802631612885822800244581533935335026869906110545776499962170319780283802669663809106916170169547105655150024437788000",
)
print(
    solution.recursive_grid_traveler(200, 200),
    "Expected:25802631612885822800244581533935335026869906110545776499962170319780283802669663809106916170169547105655150024437788000",
)
