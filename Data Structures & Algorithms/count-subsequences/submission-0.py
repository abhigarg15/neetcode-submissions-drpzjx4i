class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dfs(i,j):
            if j == len(t):
                return 1  #we are completed with the sub sequence

            if i == len(s):
                return 0 # string s is exhausted

            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
            
            return res 


        return dfs(0,0)