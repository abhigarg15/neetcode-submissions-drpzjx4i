class Solution:
    def longestPalindrome(self, s: str) -> str:
        # resIdx = 0
        # resLen = 0
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # for i in range(n-1,-1,-1):
        #     for j in range(i,n): # j will always be greater than i
        #         if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
        #             # print(s[i:j+1])
        #             dp[i][j] = True
        #             # print(dp)
        #             if resLen < (j-i+1):
        #                 resIdx = i
        #                 resLen = j - i + 1
        # return s[resIdx:resIdx + resLen]
        if len(s) <= 1:
            return s
        n = len(s)
        resLen = 0
        ans = ""
        for i in range(n):
            l,r = i,i
            while l>=0 and r<n and s[l] == s[r]:
                if resLen < r - l + 1:
                    ans = s[l:r+1]
                    resLen = r - l + 1

                l-=1
                r+=1
            
            l,r = i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    ans = s[l:r+1]
                l-=1
                r+=1

        return ans

            

