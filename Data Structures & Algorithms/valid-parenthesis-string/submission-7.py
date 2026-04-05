class Solution:
    def checkValidString(self, s: str) -> bool:
        

        # leftPar = rightPar = star = 0

        # for i in s:
        #     if left

        """
        With recursion we have 3^n possibilities
        """
        dp = {}
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if (i,open) in dp:
                return dp[(i,open)]
            
            if s[i] == "(":
                dp[(i,open)] = dfs(i+1,open + 1)
                return dp[(i,open)]
            
            if s[i] == ")":
                dp[(i,open)] = dfs(i+1, open - 1)
                return dp[(i,open)]
            
            if s[i] == "*":
                dp[(i,open)] = dfs(i+1,open+1) or dfs(i+1,open-1) or dfs(i+1,open)
                return dp[(i,open)]

        return dfs(0,0)





        