class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def rec(i):
            if i >= n:
                return i == n
            elif i in cache:
                return cache[i]
            
            cache[i] = rec(i+1) + rec(i+2)

            return cache[i]
        
        return rec(0)

