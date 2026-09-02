class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First attemp Brute Force 
        #  max_profit = 0
        #  for i in range(0, len(prices) - 1):
        #      diff = max(prices[i+1::]) - prices[i]
        #      max_profit = max(max_profit, diff)

        # Second attemp Dynamic Programming
        min_price = 100
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit