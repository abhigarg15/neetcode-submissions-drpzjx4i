class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [-1]*(n+1)
        def rec(i):
            print(i)
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = min(rec(i+1),rec(i+2)) + cost[i]
            return dp[i]

        return min(rec(0),rec(1)) # since we can start from either of the locations

