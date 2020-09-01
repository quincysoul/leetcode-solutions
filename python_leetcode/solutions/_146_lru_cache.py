"""
NOTICE
This solution is stripped from leetcode's book.

Why?
Because it is the simplest solution with O(1) time - you should NOT
be overcomplicating it.

The data structure of ordered dictionary is present in many languages-
python, javascript (as map), powershell even has it...

The implementation of this datastructure has a doubly-linked list with 
the dictionary object as well.

If they **questioned** a python solution such as this, but the position will 
involve javascript, then simply demonstrating it with javascript Map to show it is the 
exact same, should be sufficient!
"""
from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
