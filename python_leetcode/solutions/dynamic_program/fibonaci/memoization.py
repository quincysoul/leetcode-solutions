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
    def memo_fibonaci(self, n, memo=[0, 1, 1]) -> int:
        """
        Return the int which occurs at n in fibonacci sequence.
        Sample:
        __n=1, 2, 3, 4, 5
        res=1, 1, 2, 3, 5
        """

        if n == 1 or n == 2:
            return 1
        if n < len(memo):
            return memo[n]

        memo.append(self.memo_fibonaci(n - 1) + self.memo_fibonaci(n - 2))
        return memo[n]


solution = Solution()

print(solution.memo_fibonaci(50))

