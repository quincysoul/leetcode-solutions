"""[summary]

Time Complexity: [O(N)]
    1. O(N) to check each stock value left to right
    2. O(1) to calculate max profit and min price attainable
Space Complexity: [O(1)]
    * O(max_profit + min_price + current_price)
Returns:
    int: max_profit of buying and selling a stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_profit = 0
        
        for price in prices:
            if min_price is None:
                min_price = price
                
            if min_price < price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price
        
        
        if max_profit < 1:
            return 0
        else:
            return max_profit