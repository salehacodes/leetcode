class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            profit = price - min_price
            if price < min_price:
                min_price = price
            elif profit > max_profit:
                max_profit = profit
        return max_profit
            