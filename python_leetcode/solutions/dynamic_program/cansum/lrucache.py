from functools import lru_cache

"""[summary]
Problem: Write a function `canSum(targetSum, numbers)` that takes
in a targetSum and an array of numbers as arguments.

Time Complexity: [O
    1. 
Space Complexity: [O
    * 
Returns:
    bool: Is the target sum possible given the array of numbers.
"""


class Solution:
    def listToTuple(function):
        def wrapper(*args):
            args = [tuple(x) if type(x) == list else x for x in args]
            result = function(*args)
            result = tuple(result) if type(result) == list else result
            return result

        return wrapper

    @listToTuple
    @lru_cache(None)
    def recursive_can_sum(self, targetSum: int, numbers: list) -> int:
        """
        Returns bool for if the targetSum possible,
        given the array of numbers.
        """
        if targetSum < 0:
            return False

        for index, element in enumerate(numbers):
            if numbers[index] == 1:
                return True
            if numbers[index] == 2 and targetSum % 2 == 0:
                return True
            if numbers[index] == targetSum:
                return True
            if targetSum % numbers[index] == 0:
                return True
            if self.recursive_can_sum(targetSum - element, numbers) == True:
                return True

        return False
