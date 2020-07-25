// TIME: O(N)
//
// SPACE: O(N)
//
//

// First, we define what a node is, and what a Single linked list might look like.
class ListNode {
  constructor(next, val) {
    this.next = next;
    this.val = val;
  }
}
class SingleLinkedList {
  constructor(head, tail) {
    this.head = head;
    this.tail = tail;
  }
}

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

const hasCycle = function (head) {
  let node = head;
  const viewedNode = {};
  let pos = 0;
  const arrayReturn = [];

  while (node) {
    if (node.position != null) {
      // return arrayReturn,node.position;
      return true;
    }

    node.position = pos;
    // viewedNode[node.position] = node.val;
    // arrayReturn.push(node.val);

    node = node.next;
    pos++;
  }
  return false;
};
