class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)

        
        return dfs(0) # I am at 0 and can either go to 1 or 2

