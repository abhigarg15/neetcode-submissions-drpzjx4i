class Solution:
    def countSubstrings(self, s: str) -> int:
        # n = len(s)
        # res = 0 # stores how many palindromic substrings i have

        # dp = [[False]*n for _ in range(n)]
        
        # for i in range(n-1,-1,-1):
        #     for j in range(i,n):
        #         if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             res+=1

        # return res
        def func(s,l,r):
            ans = 0
            while l>=0 and r<n and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
            return ans


        n = len(s)
        res = 0
        for i in range(n):
            res += func(s,i,i)
            res += func(s,i,i+1)

        return res