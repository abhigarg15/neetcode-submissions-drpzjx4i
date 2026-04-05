class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        dp = {}

        def rec(i):
            if i >= len(cost):
                return 0
            elif i in dp:
                return dp[i]

            dp[i] = cost[i] + min(rec(i+1), rec(i+2))

            return dp[i]
            


        return min(rec(0),rec(1))