/**
 * Time Complexity: [O(N)]
 *    Loops over heights in arra at O(N) multiplies by width, and checks maximum area.
 * Space Complexity: [O(1)]
 *    Nothing complicated.
 * Trick: You do not have to look at every possible window, only the windows
 * which could have a taller height to collect more water.
 */
function maxArea(height) {
  let max = 0;

  let L = 0;
  let R = height.length - 1;
  let width = height.length - 1;

  while (L < R) {
    let area = 0;
    if (height[L] < height[R]) {
      area = height[L] * width;
      width--;
      L++;
    }
    else {
      area = height[R] * width;
      width--;
      R--;
    }
    if (area > max) {
      max = area;
    }
  }

  return max;
}
export default maxarea;
