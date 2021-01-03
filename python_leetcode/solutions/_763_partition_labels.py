"""[summary]

Time Complexity: [O(N)]
    1. O(N) iteration to determine end index for each character in dic
    2. O(N) iteration to determine L,R bounds for each character at index
Space Complexity: [O(1)]
    * O(possible_characters_count).
Returns:
    List: a list of the lengths of each range as demonstrated
          in below comment, each range is the max range allowing
          a character only in one range. Ex [8,1,3,1]
"""


"""
 0  1  2  3  4  5  6  7  8  9 10 11 12 13
"a, b, a, b, c, b, a, c, a, d, e, f, e, g"
 L
                         R
                         i
"a, b, a, b, c, b, a, c, a,
                            d, 
                               e, f, e
                                        g
{ 
a:8 b:5 c:7 d:9 e:12 f:11 g:13
}
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        char_end_indexes = {}
        for index, element in enumerate(S):
            char_end_indexes[element] = index

        L = 0
        R = 0

        for index, element in enumerate(S):
            R = max(char_end_indexes.get(element), R)
            if index == R:
                res.append(R - L + 1)
                R += 1
                L = R
        return res

