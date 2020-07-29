import missingNumber from '../268-missingNumber';

describe('missingNumber will look in array of length n for \
a the number missing (numbers are 0 - n).', () => {
  test('it should find a missing number', () => {
    const nums = [0, 1, 2, 3, 5];

    expect(missingNumber(nums)).toEqual(4);
  });

  test('it should find a missing number', () => {
    const nums = [0, 3, 5, 8, 4, 6, 1, 9, 7];

    expect(missingNumber(nums)).toEqual(2);
  });
});
