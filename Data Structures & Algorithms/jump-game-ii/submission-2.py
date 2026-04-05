class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]

        #     if i >= len(nums)-1:
        #         return 0
            
        #     res = float("inf")
        #     for j in range(i+1, i+nums[i]+1):
        #         res = min(res,dfs(j)+1)
        #     dp[i] = res
        #     return res
        # return dfs(0)


        l = r = res = 0

        while r < len(nums)-1: # the moment it becomes r == len(nums)-1 we got our goal
            farthest = 0
            for j in range(l,r+1):
                farthest = max(farthest, j + nums[j])
            l = r+1
            r = farthest 
            res+=1
        
        return res
