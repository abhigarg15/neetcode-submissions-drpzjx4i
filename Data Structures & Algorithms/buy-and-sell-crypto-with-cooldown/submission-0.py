class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i,buying):
            if i >= len(prices):
                return 0 # no profit or loss

            cooldown = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                return max(cooldown,buy)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                return max(sell,cooldown)

        return dfs(0,True)