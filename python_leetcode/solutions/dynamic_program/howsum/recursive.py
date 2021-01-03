"""[summary]
Problem: Write a function `howSum(targetSum, numbers)` that takes
in a targetSum and an array of numbers as arguments.

Time Complexity: [O
    1. 
Space Complexity: [O
    * 
Returns:
    list: That adds up to the targetSum. If not possible, return None
"""


class Solution:
    # def __init__(self):
    #     print("NEW INSTANCE")

    # def __new__(self):
    #   print("NEW")

    def recursive_howsum(self, targetSum: int, numbers: list) -> list:
        """
        Returns any possible combination of numbers from `numbers` in a list
        that equals target sum.
        """
        if targetSum == 0:
            return []
        if targetSum < 0:
            return None

        for index, element in enumerate(numbers):
            # print(f"comparing {element}/{targetSum}")
            remainder = targetSum - element

            res = self.recursive_howsum(remainder, numbers)
            if res is not None:
                res.append(element)
                return res
