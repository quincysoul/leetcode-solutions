/**
 * Time Complexity: [O(N)]
 *    Loops over characters in string at O(N), and does O(1) evaluations.
 * Space Complexity: [O(N)]
 *    It is O(N) if string is stored as string.trim(), but also the
 *    converted int will require up to O(N) space per each character converted.
 *    However, if you take into account the requirement of INT_MIN and INT_MAX,
 *    and remove string.trim()
 *    for more complicated iteration, you can do in O(1) as it is reduced from O(SIGNED_INT_RANGE)
 */
function myAtoi(string) {
  const stringModified = string.trim('');
  // Cost: O(N)

  const spaceChar = ' ';
  const acceptedChars = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
  };
  const intMax = (2 ** 31) - 1;
  const intMin = -(2 ** 31);

  let signInt = 1;
  let multiplier = 1;
  let convertedInt = 0;
  let modifiedInt = false;
  let i = 0;
  if (stringModified == null || stringModified.length === 0) { return 0; }
  if (stringModified[0] === '-') {
    signInt = -1;
    i = 1;
    modifiedInt = true;
  }
  if (stringModified[0] === '+') {
    i = 1;
    modifiedInt = true;
  }
  for (i; i < stringModified.length; i++) {
    const currentChar = stringModified.charAt(i);
    if (currentChar === spaceChar && !modifiedInt) {
      // eslint-disable-next-line no-continue
      continue;
    } else if (acceptedChars[currentChar] != null) {
      multiplier = 10;
      convertedInt *= multiplier;
      convertedInt += acceptedChars[currentChar];
      modifiedInt = true;
    } else {
      break;
    }
  }
  convertedInt *= signInt;
  if (convertedInt > intMax) { return intMax; }
  if (convertedInt < intMin) { return intMin; }

  return convertedInt;
}

export default myAtoi;
