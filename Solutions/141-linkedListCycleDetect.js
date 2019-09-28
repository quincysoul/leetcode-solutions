// TIME: O(N)
//
// SPACE: O(N)
//
//

//First, we define what a node is, and what a Single linked list might look like.
class ListNode
{
    constructor(next,val)
    {
        this.next = next;
        this.val = val;
    }
}
class SingleLinkedList
{
    constructor(head,tail)
    {
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

var hasCycle = function(head) {
    
    let node = head;
    let viewedNode = {};
    let pos = 0;
    let arrayReturn = [];

    while(node)
    {
      if(node.position !=null)
      {
         // return arrayReturn,node.position;
        return true;
      }
      else
      {
        node.position = pos;  
        // viewedNode[node.position] = node.val;
        // arrayReturn.push(node.val);

        node = node.next;
        pos++;
      }
    }
  return false;
};