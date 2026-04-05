class Solution:
    def jump(self, nums: List[int]) -> int:


        def dfs(i):
            if i >= len(nums)-1:
                return 0
            res = float("inf")
            for j in range(i+1, i+nums[i]+1):
                res = min(res,dfs(j)+1)
            
            return res

        return dfs(0)