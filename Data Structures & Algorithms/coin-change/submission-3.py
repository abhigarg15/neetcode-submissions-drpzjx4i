class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = defaultdict()

        # def rec(amount):
        #     if amount == 0 :
        #         return 0
            
        #     if amount in memo:
        #         return memo[amount]
            
        #     res = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + rec(amount - coin))
        #     memo[amount] = res
        #     return memo[amount]
            
        # minCoins = rec(amount)
        # if minCoins >= 1e9:
        #     return -1
        
        # return minCoins
        # res = 1e9
        dp = {}
        def rec(amount):
            if amount == 0:
                return 0 # no more coins necessary

            if amount in dp:
                return dp[amount]
            res = int(1e9)
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + rec(amount - coin) )

            dp[amount] = res
            return dp[amount]
        res = rec(amount)
        return -1 if res >= 1e9 else res