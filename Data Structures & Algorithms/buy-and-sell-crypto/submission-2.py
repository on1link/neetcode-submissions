class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First attemp Brute Force 
        #  max_profit = 0
        #  for i in range(0, len(prices) - 1):
        #      diff = max(prices[i+1::]) - prices[i]
        #      max_profit = max(max_profit, diff)

        # Second attemp Dynamic Programming
        # min_price = 100
        # max_profit = 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit
        
        # Two pointers
        # left_p = buy
        # right_p = sell
        left_p = 0
        right_p = 1 
        max_p = 0

        while right_p < len(prices):
            buy = prices[left_p]
            sell = prices[right_p]
            if buy < sell:
                max_p = max(max_p, prices[right_p] - prices[left_p])
            else:
                left_p = right_p
                
            right_p +=1

        return max_p
        