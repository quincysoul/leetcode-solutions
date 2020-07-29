import numberToWords from '../237-intToWords';

describe('numToWords should take an integer and return an english version of the integer up tothe billions place.', () => {
  test('it should return a english version of the int', () => {
    const int = 123456;

    expect(numberToWords(int)).toEqual('One Hundred Twenty Three Thousand Four Hundred Fifty Six');
  });

  test('it should return a english version of the int2', () => {
    const int = 12345;

    expect(numberToWords(int)).toEqual('Twelve Thousand Three Hundred Forty Five');
  });
});
