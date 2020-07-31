/**
 * Time Complexity: [O(N)]
 *   1. Iterate through O(N) elements.
 * Space Complexity: [O(1)]
 *    Elements are swapped in place.
 * Trick:
 *    When approaching a "binary" type sorting check if going forward or backwards is easier.
 *    This problem, I used forwards.
 *    Swapping array elements gets this near optimal.
 */
const moveZeroes = function (nums) {
  let nonZeroIndex = -1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      const temp = nums[nonZeroIndex + 1];
      nums[nonZeroIndex + 1] = nums[i];
      nums[i] = temp;
      nonZeroIndex++;
    }
  }
  return nums;
};
export { moveZeroes };
