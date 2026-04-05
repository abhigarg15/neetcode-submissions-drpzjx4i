class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # goal is to reach len(cost)
        # cache = [-1]*len(cost)
        # def rec(i):
        #     if i >= len(cost):
        #         return 0
            
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = cost[i] + min(rec(i+1),rec(i+2))
        #     return cache[i]

        # return min(rec(0),rec(1))

        n = len(cost)
        dp = [0]*(n+1)
        for i in range(2,n+1):
            dp[i] = min(dp[i-1] + cost[i-1], 
                        dp[i-2] + cost[i-2])
        
        return dp[n]