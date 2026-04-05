class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # b = prices[0]
        # for i in range(1,len(prices)):
        #     profit = max(profit,prices[i]-b)
        #     b = min ( prices[i],b)

        # l,r = 0,1

        # profit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = max(profit,prices[r]-prices[l])
        #     else:
        #         l = r
             
        #     r += 1

        # return profit
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            buy = min(buy, prices[i])            
            profit = max(profit, prices[i] - buy)

        return profit











