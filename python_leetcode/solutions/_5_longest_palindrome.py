class Solution:
    def longestPalindrome(self, s: str) -> str:

        R = 0
        C = 0
        S = ["#"]
        max_p_dist = 0
        max_index = 0

        for ch in s:
            S += ch, "#"

        P = [0 for _ in range(len(S))]

        # print(f"S: {S}")
        # print(f"P: {P}")

        for i in range(len(S)):

            # print(f"i: {i}---------------")
            if i >= R + C:
                C = i
            if i == C:
                # print(f"i==C.")
                j = 1
                p_dist = 0
                try:
                    while S[i + j] == S[i - j]:
                        j += 1
                        p_dist += 1
                except:
                    pass
                # print(f"p_dist: ${p_dist}")
                P[i] = p_dist
                R = p_dist
            if i < C + R:
                # Inside of palindrome.
                left_mirror_index = C - (i - C)
                left_mirror_element = P[left_mirror_index]
                P[i] = min(R + C - i, left_mirror_element)
            if P[i] > max_p_dist:
                max_p_dist = P[i]
                max_index = i

        res = ""
        # print(f"P max index: {max_index}")
        # print(f"P ending: {P}")

        for i in range((P[max_index] * 2) + 1):
            if S[max_index - P[max_index] + i] != "#":
                res += S[max_index - P[max_index] + i]

        return res

        # i:   [00,01,02,03,04,05,06,07,08,09,10]
        # str: [# ,a ,# ,c ,# ,a ,# ,c ,# ,a ,# ]
        # P:   [00,01,00,00,00,05,00,00,00,00,00]
        # R:   [  ,  ,  ,  ,  ,  ,   ],
