class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution 1] This solution was based out of simple recursion
        """
        # def dfs(i):
        #     print(i)
        #     if i >= n:
        #         return i == n
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0) # I am at 0 and can either go to 1 or 2

        """
        Solution 2] This solution is based on Top down DP
        """
        cache = [-1]*n
        def rec(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]

            cache[i] = rec(i+1) + rec(i+2)
            return cache[i]

        return rec(0)

