"""[summary]
Problem: given a number n return the fibonnaci number.

Time Complexity: [O(2 ** n)]
    1. 
Space Complexity: [O(N)]
    * 
Returns:
    int: fibonacci number at n.
"""


class Solution:
    def recursive_fibonaci(self, n) -> int:
        """
        Return the int which occurs at n in fibonacci sequence.
        Sample:
        __n=1, 2, 3, 4
        res=1, 1, 2, 3, 5
        """

        if n == 1 or n == 2:
            return 1

        return self.recursive_fibonaci(n - 1) + self.recursive_fibonaci(n - 2)
