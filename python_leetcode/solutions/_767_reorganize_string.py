"""[summary]

Time Complexity: [O(N * log(A) )]
    1. O(N) to count string
    2. O(A) number of characters that can be on heap (unique alpha)
Space Complexity: [O(A)]
    * O(A) number of characters that can be counted and on heap.
Returns:
    build_string: Re-organized string
"""
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        build_string = ""
        heap = []
        char_count = { ch:0 for ch in "abcdefghijklmnopqrstuvwxyz" }
        
        for ch in S:
            char_count[ch] += 1

        for ch in char_count:
            if char_count[ch] > 0:
                heapq.heappush( heap, [-char_count[ch],ch] )

        prev_char = None
        while heap:
            ch_1_element = heapq.heappop(heap)
            ch_1_ch = ch_1_element[1]
            
            if prev_char == ch_1_ch or prev_char == "":
                return ""
                
            ch_2_ch = ""
            if heap:
                ch_2_element = heapq.heappop(heap)
                ch_2_ch = ch_2_element[1]
                
                #Decrement count
                ch_2_element[0] += 1
                if ch_2_element[0] < 0:
                    heapq.heappush( heap, [ch_2_element[0], ch_2_ch])

            #Decrement count
            ch_1_element[0] += 1
            if ch_1_element[0] < 0:
                heapq.heappush( heap, [ch_1_element[0], ch_1_ch])
                
            build_string += ch_1_ch
            build_string += ch_2_ch
            
            prev_char = ch_2_ch
        return build_string