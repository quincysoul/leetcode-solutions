/**
 * Time Complexity: [O(N)]
 *   1. Iterate through O(N) indices.
 *   2. Each element should be equal to i.
 *      if element != n, attempt to swap up to N times
 *      Each swap makes the iteration over the corrected element
 *      Not require a swap - so the max swaps occurring across the entire array is O(N).
 *      This therefore remains linear and totals O(2N) -> O(N)
 * Space Complexity: [O(1)]
 *    Temp storage of elements being viewed
 *    Temp storage of elements being swapped
 *    Temp storage of null index.
 * Trick:
 *    Problem can be sorted in O(N) due to basic expected elements.
 */
function missingNumber(nums) {
  nums.push(null);
  const range = nums.length;
  let nullIndex = -1;

  for (let i = 0; i < range; i++) {
    if (nums[i] == i) {
    }
    else if (nums[i] === null) {
      nullIndex = i;
    }
    else {
      while (nums[i] !== null && nums[i] != i) {
        const temp = nums[nums[i]];
        nums[nums[i]] = nums[i];
        nums[i] = temp;

        if (nums[nums[i]] === null) {
          nullIndex = nums[i];
        }
        if (nums[i] === null) {
          nullIndex = i;
        }
      }
    }
  }
  return nullIndex;
}
export default missingNumber;
