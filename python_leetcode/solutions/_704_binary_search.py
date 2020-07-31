import bisect

"""[summary]

Time Complexity:
    O( log(N)
Returns:
    [type]: [description]
"""


class Solution:
    def search(self, nums, target: int) -> int:
        """[summary]

        Args:
            nums (List[int]): sorted array with any ints.
            target (int): element to search for.
        Returns:
            int: index of first occurrence of target.
        """
        index = bisect.bisect_left(nums, target, 0, len(nums))
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def bisect_left_impl(self, array, target, start=0, end=None):
        if start < 0:
            raise ValueError("Start must be non-negative.")
        if end is None:
            end = len(array)

        # i:0  1  2  3   4   5   6
        # _[0, 1, 2, 24, 24, 24, 25]
        # i|target 2:
        # 0[s,  ,  ,  m,   ,   ,   ]e
        # 1[s,  ,  , em,   ,   ,   ]
        # 2[ , m, s,  e,   ,   ,   ]
        # 2[ ,  ,sme,  ,   ,   ,   ]
        while start < end:
            mid = (start + end) // 2
            if array[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    def search_with_bisect_impl(self, nums, target):
        index = Solution.bisect_left_impl(self, nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
