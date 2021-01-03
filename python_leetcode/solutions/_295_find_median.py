import heapq

"""[summary]

Time Complexity: [O(log N)]
    * O(logN) per heap push
    * O(1) per heap top
    * O(logN) per heap pop
Space Complexity: [O(N)]
    * Space inceases by N inputs of ints.
Returns:
    [int]: [median of the list of ints provided thus far]
"""


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]

    def addNum(self, int):
        # Going to use max_heap to store medians,
        # And then when equal length,
        # (min_heap[0] + max_heap[0]) / 2 is our median

        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, int)
        else:
            if int <= self.min_heap[0]:
                heapq.heappush(self.max_heap, -int)
            else:
                heapq.heappush(self.min_heap, int)

            self.balance()

    def balance(self):
        if len(self.max_heap) == len(self.min_heap) + 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) == len(self.max_heap) + 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

            print(f"balanced... min:{self.min_heap[0]}max:{self.max_heap[0]}")
