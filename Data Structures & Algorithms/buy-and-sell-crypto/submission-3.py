class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100000
        profit = 0
        for price in prices:
            lowest = min(price, lowest)
            profit = max(profit, price -lowest)
        return profit