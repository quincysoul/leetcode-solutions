"""[summary]
Problem: Write a function `bestSum(targetSum, numbers)` that takes
in a targetSum and an array of numbers as arguments. Return the least
length array of combination to get the sum. Or None if not possible.

Time Complexity: [O
    1. 
Space Complexity: [O
    * 
Returns:
    list: That adds up to the targetSum. If not possible, return None
"""


class Solution:
    def __init__(self):
        self.min_best_sum_len = float("inf")
        self.min_best_sum_arr = []

    # def __new__(self):
    #   print("NEW")

    def recursive_bestsum(self, targetSum: int, numbers: list) -> list:
        """
        Returns any possible combination of numbers from `numbers` in a list
        that equals target sum.
        """

        if targetSum == 0:
            return []
        if targetSum < 0:
            return None

        min_best_len = float("inf")
        shortest_res = None

        for element in numbers:
            remainder = targetSum - element

            res = self.recursive_bestsum(remainder, numbers)
            if res is not None:
                res.append(element)
                if len(res) < min_best_len:
                    shortest_res = res

        return shortest_res
