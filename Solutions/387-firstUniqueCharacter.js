class Que {
  constructor() {
    this.que = [];
    this.front = 0;
  }

  peekFront() {
    if (this.que.length - this.front > 0) {
      return this.que[this.front];
    }
    return null;
  }

  enque(element) {
    this.que.push(element);
  }

  deque() {
    this.front += 1;
  }
}

function firstUniqChar(string) {
  const que = new Que();
  const hashTable = {};

  [...string].forEach((char, index) => {
    if (hashTable[char]) {
      const queFrontChar = string[que.peekFront()];
      if (char === queFrontChar) {
        que.deque();
      }
    }
    else {
      que.enque(index);
      hashTable[char] = true;
    }
  });

  if (que.peekFront() == null) {
    return -1;
  }
  return que.peekFront();
}

firstUniqChar('leetcode');
