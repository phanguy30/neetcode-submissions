class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buying):
            # Base case: if we've passed the last day
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                # Choice 1: Buy today (move to sell state, subtract price)
                # Choice 2: Skip today (stay in buy state)
                buy_today = dfs(i + 1, False) - prices[i]
                skip_buy = dfs(i + 1, True)
                memo[(i, buying)] = max(buy_today, skip_buy)
            else:
                # Choice 1: Sell today (must skip a day, move to buy state, add price)
                # Choice 2: Skip selling (stay in sell state)
                sell_today = dfs(i + 2, True) + prices[i]
                skip_sell = dfs(i + 1, False)
                memo[(i, buying)] = max(sell_today, skip_sell)
            
            return memo[(i, buying)]
            
        return dfs(0, True) # Start at day 0, looking to buy