class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if i in dp:
                return dp[i]
            for j in range(i+1, i + nums[i] + 1):
                if dfs(j):
                    dp[i] = True
                    return True  
            dp[i] = False
            return False

        return  dfs(0)