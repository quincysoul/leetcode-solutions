"""[summary]

Time Complexity: [O(N)]
    1. O(N) to count each color.
    2. O(N) to iterate over array and rewrite each element.
    O(2n) -> O(N)
Space Complexity: [O(1)]
    * O(possible colors) + O(max counts)
Returns:
    [type]: [description]
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        numsIndex = 0
        for color in range(3):
            if color in count:
                for j in range(count[color]):
                    nums[numsIndex] = color
                    numsIndex += 1

