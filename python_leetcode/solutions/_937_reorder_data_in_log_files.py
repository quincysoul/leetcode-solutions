"""[summary]

Time Complexity: [O(N log N)]
    1. O(N) to iterate over each log and determine types.
    2. O(N log N) to run python's sort (timsort)
Space Complexity: [O(1)]
    * O(max_profit + min_price + current_price + max_profit_sum)
Returns:
    int: max_profit of buying and selling a stock
"""


class Solution:
    def reorderLogFiles(self, logs):
        # First word is id
        # Every word after ID will be:
        # a. [a-z ]
        # b. [0-9 ]
        # 1. Reorder so A list is before B list.
        # 2. Sort A list lexocographically
        # NOTICE: python sort() is lexocographic by default
        # js> sort is not, it is comparator.
        # if a letter log is tied, use the ID to sort.
        # 3. Do not sort B list.
        # 4. Return a list of the logs in said order.

        letter_logs = []
        number_logs = []

        for log in logs:
            splitted = log.split(" ")

            if splitted[1][0].isalpha():
                letter_logs.append(log)
            else:
                # elif isnumeric():
                number_logs.append(log)

        new_list = sorted(letter_logs, key=self.letter_log_keyer)
        new_list.extend(number_logs)
        return new_list

    def letter_log_keyer(self, log):
        # NOTE: python allows sorting by more than one option, if the first option is tied.
        # Return to the key caller a tuple. It will attempt sort on each element,
        # and if tied try next element, in the key tuple.
        return (log.split(" ")[1:], log.split(" ")[:1])

