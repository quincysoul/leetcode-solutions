import stringToIntAtoi from '../8-stringToIntAtoi';

describe('stringToIntAtoi - it should convert string to int.', () => {
  test('it removes space characters.', () => {
    const input = '  43';

    expect(stringToIntAtoi(input)).toEqual(43);
  });
  test('if it is below INT_MIN as set by problem, return INT_MIN (−231)', () => {
    const intMax = (2 ** 31) - 1;
    const intMin = -(2 ** 31);
    const tooHigh = intMax + 1;
    const tooLow = intMin - 1;

    expect(stringToIntAtoi(tooLow.toString())).toEqual(intMin);
  });
  test('if it is above INT_MAX as set by problem, return INT_MAX (−231)', () => {
    const intMax = (2 ** 31) - 1;
    const intMin = -(2 ** 31);
    const tooHigh = intMax + 1;
    const tooLow = intMin - 1;

    expect(stringToIntAtoi(tooHigh.toString())).toEqual(intMax);
  });

  test('it should handle empty strings', () => {
    expect(stringToIntAtoi('')).toEqual(0);
  });

  test('it should handle negative numbers', () => {
    expect(stringToIntAtoi(' -123')).toEqual(-123);
  });

  test('it should stop parsing as soon as hitting invalid characters (valid is - or space)', () => {
    expect(stringToIntAtoi('w15')).toEqual(0);
  });

  test('it should stop parsing as soon as hitting invalid characters (valid is - or space)', () => {
    expect(stringToIntAtoi('15w')).toEqual(15);
  });

  test('it should stop parsing as soon as hitting invalid characters (valid is - or space)', () => {
    expect(stringToIntAtoi(' -15w20')).toEqual(-15);
  });
});
