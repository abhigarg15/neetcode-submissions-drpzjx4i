class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # if len(nums) == 1:
        #     return nums[0]

        # n = len(nums)
        # dp = [0]*(n)

        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])

        # for i in range(2,n):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        # return dp[-1]

        # n = len(nums)
        # dp = [-1]*n
        # def rec(i):
        #     if i >= len(nums):
        #         return 0 

        #     if dp[i] != -1:
        #         return dp[i]

        #     dp[i] = max(rec(i+2) + nums[i], rec(i+1))

        #     return dp[i]

        # return rec(0)

        dp = {}

        def dfs(i):
            if i >= len(nums):
                return 0 # not gold accumulated
            elif i in dp:
                return dp[i]
            ans = max(nums[i] + dfs(i+2), dfs(i+1))
            dp[i] = ans

            return dp[i]

        return dfs(0)
"""
    [1,1,3,7]

""" 
