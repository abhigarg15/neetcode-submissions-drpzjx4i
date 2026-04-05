class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i):
            if i >= len(nums)-1:
                return True
            print(i)
            for j in range(i+1, i + nums[i] + 1):
                if dfs(j):
                    return True    

            return False

        return  dfs(0)