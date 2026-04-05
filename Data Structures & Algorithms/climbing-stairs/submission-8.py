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
        # cache = [-1]*n
        # def rec(i):
        #     if i >= n:
        #         return i == n
        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = rec(i+1) + rec(i+2)
        #     return cache[i]

        # return rec(0)

        # def rec(n):
        #     if n <= 0:
        #         return 1
        #     if n == 1:
        #         return 1

        #     return rec(n-1) + rec(n-2)

        # return rec(n)

        # cache = [-1]*n
        # def dfs(i):
        #     if i>=n:
        #         return i == n
        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = dfs(i+1) + dfs(i+2)
        #     print(cache)
        #     return cache[i]


        # return dfs(0)

        # if n<=2:
        #     return n

        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]
        """
        space optimized final most optimized solutions
        """
        # one = 1
        # two = 1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp

        # return one


        """
        Trying recursion solution again
        """



        def rec(i):
            if i == 1:
                return 1
            if i == 2:
                return 2

            return rec(i-1) + rec(i-2)


        return rec(n)
