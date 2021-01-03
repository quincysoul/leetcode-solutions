"""[summary]

Time Complexity: [O(1)]
    1. O(
Space Complexity: [O(N)]
    * O(
Returns:
    [type]: [description]
"""


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.list = []
        """
        So for the list, it contains the num in a set.
        [
            #0  1  2  3    4    
             0, 1, 2, 1000, 400,
        ]
        for the dic, it contains the index of that value in the list
        {
            0:0, 1:1, 2:2, 400:4, 1000:5
        }

        [

        ]
        {
        }

        """

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.dic.get(val) is None:
            self.list.append(val)
            self.dic[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.dic.get(val) is not None:
            index_of_item_to_remove = self.dic.get(val)
            index_of_replacement = len(self.list) - 1
            self.list[index_of_item_to_remove] = self.list[index_of_replacement]

            self.list.pop()
            del self.dic[val]
            if index_of_item_to_remove < len(self.list):
                value_of_replacement = self.list[index_of_item_to_remove]
                self.dic[value_of_replacement] = index_of_item_to_remove

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
