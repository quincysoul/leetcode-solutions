from functools import lru_cache

"""[summary]
Problem: given a number n return the fibonnaci number.

Time Complexity: [O(N)]
    1. 
Space Complexity: [O(N)]
    * 
Returns:
    int: fibonacci number at n.
"""


class Solution:
    # memo is a memoization array...
    @lru_cache(None)
    def lrucache_fibonaci(self, n) -> int:
        """
        Return the int whic2h occurs at n in fibonacci sequence.
        Sample:
        __n=1, 2, 3, 4, 5, 6,  7,
        res=1, 1, 2, 3, 5, 8, 13
        """

        if n == 1 or n == 2:
            return 1

        return self.lrucache_fibonaci(n - 1) + self.lrucache_fibonaci(n - 2)


solution = Solution()

print(solution.lrucache_fibonaci(5), "expected 5")

print(solution.lrucache_fibonaci(7), "expected 13")

print(solution.lrucache_fibonaci(50), "expected 12586269025")
