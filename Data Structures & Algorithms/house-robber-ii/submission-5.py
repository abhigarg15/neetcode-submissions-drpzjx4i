class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]

        # n = len(nums)
        # dp = [[-1]*2 for _ in range(n)]
        
        
        # def rec(i,flag):
        #     if (flag and i == n-1) or i >= n :
        #         return 0
        #     if dp[i][flag] != -1:
        #         return dp[i][flag]
        #     dp[i][flag] = max(rec(i+1,flag),
        #                 nums[i] + rec(i+2,flag or i == 0))
        #     return dp[i][flag]

        

        # return max(rec(0,True), rec(1,False))

        if len(nums) == 1:
            return nums[0]

        dp = {}
        def dfs(i,flag):
            if (flag and i == len(nums)-1) or i >= len(nums):
                return 0
            
            if (i,flag) in dp:
                return dp[(i,flag)]

            dp[(i,flag)] = max(nums[i]+dfs(i+2,flag or i == 0), dfs(i+1,flag))

            return dp[(i,flag)]

        return max(dfs(0,True), dfs(1,False))

            
            
