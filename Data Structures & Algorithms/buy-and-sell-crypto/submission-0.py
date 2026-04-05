class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        profit = 0
        b = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-b)
            b = min ( prices[i],b)


        return profit