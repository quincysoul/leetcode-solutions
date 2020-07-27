/**
 * Time Complexity: [O(N)]
 *    O(N) to determine middle (highest height)
 *    O(N) iteration over left and right of middle.
 *    0(2N) reduces to O(N).
 * Space Complexity: [O(1)]
 *    Only maxes and indices are temporarily stored.
 * Advisory:
 *    Draw the sample out on a whiteboard.
 *    Observe that between the most highest index, you can store
 *    x water between that and the ending right index. Store the
 *    current height as secondHighest (if it is equal or less than).
 *
 *    If you then go right - 1, you can only store
 *    secondHighest (from the right) - height[right-1].
 *
 *    Observe that if you hit a new secondHighest,
 *    you will never store water there, so you can move onto the right-1.
 * */
const trap = function (height) {
  let volume = 0;
  let max = 0;
  let maxIndex = -1;
  height.forEach((h, index) => {
    if (h > max) {
      max = h;
      maxIndex = index;
    }
  });

  let L = 0;
  let R = height.length - 1;
  let secondHighest = 0;
  while (L < maxIndex) {
    if (height[L] >= secondHighest) {
      secondHighest = height[L];
    }
    else {
      volume += secondHighest - height[L];
    }
    L++;
  }
  secondHighest = 0;
  while (R > maxIndex) {
    if (height[R] >= secondHighest) {
      secondHighest = height[R];
    }
    else {
      volume += secondHighest - height[R];
    }
    R--;
  }
  return volume;
};
