/**
 * Time Complexity: [O(N)]
 *   1. int.toString() in 0(N).
 *   2. numString.forEach() in O(N).
 *      check 3 elements for about 1/3 of N making O(2N)
 *   3. Pop entire stack O(N)
 *      js engine pushes stack into array in same operation
 *      array is joined into string making O(2N)
 * Space Complexity: [O(1)]
 *    Temp storage of viewed elements.
 * Trick:
 *    As with Roman numberals question, you should always rely
 *    on hash tables to ensure constant access of language/words.
 */
function numberToWords(num) {
  if (num == 0) {
    return 'Zero';
  }
  if (num == null) {
    return 'Zero';
  }
  const ones = {
    '0': '',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
  };
  const teens = {
    '': 'Ten',
    'One': 'Eleven',
    'Two': 'Twelve',
    'Three': 'Thirteen',
    'Four': 'Fourteen',
    'Five': 'Fifteen',
    'Six': 'Sixteen',
    'Seven': 'Seventeen',
    'Eight': 'Eighteen',
    'Nine': 'Nineteen',
  };
  const tens = {
    '0': '',
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Forty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety',
  };
  const hundreds = {
    '0': '',
    '1': 'One Hundred',
    '2': 'Two Hundred',
    '3': 'Three Hundred',
    '4': 'Four Hundred',
    '5': 'Five Hundred',
    '6': 'Six Hundred',
    '7': 'Seven Hundred',
    '8': 'Eight Hundred',
    '9': 'Nine Hundred',
  };

  const numString = num.toString();
  const stack = [];
  const specials = {
    '0': 'Thousand',
    '1': 'Million',
    '2': 'Billion',
  };
  /**
   *    3   2    1    0   (k)
    *   bill|mill|thou|hun (specials[k])
    *   210 |210 |210 |210 (j)
    *   123, 456, 789, 101 (hundreds[j],tens||teens[j],ones[j])
    *   // i is used for index of loop backwards or forwards.
    * */

  let j = 0;
  let k = 0;
  for (let i = numString.length - 1; i > -1; i--) {
    const element = numString[i];
    switch (j) {
      case 0: {
        stack.push(ones[element]);
        j++;
        break;
      }
      case 1: {
        if (element == 1) {
          const onesVal = stack.pop();
          stack.push(teens[onesVal]);
        }
        else {
          stack.push(tens[element]);
        }
        j++;
        break;
      }
      case 2: {
        stack.push(hundreds[element]);
        if ((numString[i - 1] != null && numString[i - 1] != 0)
            || (numString[i - 2] != null && numString[i - 2] != 0)
            || (numString[i - 3] != null && numString[i - 3] != 0)) {
          stack.push(specials[k]);
        }
        k++;
        j = 0;
        break;
      }
      default: {
        break;
      }
    }
  }
  // End numString backwards iteration.

  let finalString = '';
  const len = stack.length;
  for (let i = 0; i < len; i++) {
    const topOfStack = stack.pop();
    if (topOfStack != '') {
      finalString += `${topOfStack} `;
    }
  }

  return finalString.trim();
}
export default numberToWords;
