"""
Summary:
    Time Complexity: O(N+M)
        * Iterate over paragraph: +O(N)
        * Iterate over words: +O(N)
        * Iterate over banned words (once): O(M)
        * Push N words to heap: +O(N) (if you perform heappush exactly N times)
        * Heappop: O(logN) (too small to add)
    Space Complexity: O(N + M + h)
        * Dictionary or list of words and banned words and heap of words.
Trick:
    This is the solution which you can easily adapt to most common K words
    * You create a heap of non banned words
    * You pop the heap K times and you have the solution.
    * To get most common word, only pop heap once. 
    * Further optimizing for this one, you can do heap[0] instead of heapq.heappop().

Bibliography:
    zengtian's heapq solution

Args:
    paragraph - string which can contain whitespace and special characters.
    banned - list of lowercase words.
"""
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        res = []
        heap = []
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for word in word_count:
            heapq.heappush(heap, [-word_count.get(word), word])

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
