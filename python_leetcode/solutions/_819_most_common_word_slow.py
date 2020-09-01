import heapq

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


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = {}
        word_list = []
        res = ""
        heap = []

        for word in banned:
            banned_words[word] = True

        word = ""
        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()
                if ch == paragraph[-1]:
                    if len(word) > 0 and banned_words.get(word) != True:
                        word_list.append(word)
            else:
                if len(word) > 0 and banned_words.get(word) != True:
                    word_list.append(word)
                word = ""

        word_dict = {}
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0) + 1

        for word in word_dict:
            # Take the count value from word key, and use it to sort it in a heapq (prio q)
            heapq.heappush(heap, [-word_dict[word], word])  # ???

        if len(heap) > 0:
            res = heapq.heappop(heap)[1]

        return res
