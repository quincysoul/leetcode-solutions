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

// Time complexity: O(N) as we iterate over the list once to reverse it.

// Next we do the solution function.
const reverseList = function (head) {
  let node = head;
  let prev = null;

  while (node) {
    const tempNode = node.next;
    node.next = prev;

    prev = node;

    node = tempNode;
  }

  return prev;
};
