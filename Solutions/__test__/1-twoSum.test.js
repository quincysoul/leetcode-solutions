import { twoSum } from '../1-twoSum';

describe('twoSum - it should return an array containing the indexes of two integers\
which equal the target value, picking from input nums array.', () => {
  test('', () => {
    const nums = [0, 1, 2, 3, 4];
    const target = 6;

    expect(twoSum(nums, target)).toEqual([2, 4]);
  });
});
