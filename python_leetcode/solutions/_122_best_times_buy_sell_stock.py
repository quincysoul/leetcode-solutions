"""[summary]

Time Complexity: [O(N)]
    1. O(N) to check each stock value left to right
    2. O(1) to calculate max profit and min price attainable
    3. O(1) to sum the profits obtained
Space Complexity: [O(1)]
    * O(max_profit + min_price + current_price + max_profit_sum)
Returns:
    int: max_profit of buying and selling a stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit_sum = 0
        max_profit = 0
        min_price = None
        
        i = 0
        for price in prices:
            if min_price is None:
                min_price = price
                
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
            
            if i+1 < len(prices):
                if prices[i+1] < prices[i]:
                    max_profit_sum += max_profit
                    max_profit = 0
                    min_price = None
            else:
                max_profit_sum += max_profit
                
            i += 1
        
        return max_profit_sum