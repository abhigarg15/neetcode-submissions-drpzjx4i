class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # we need to detect the longest palindromic substring
        if len(s) <= 1:
            return s
        def isPalin(s):
            return s == s[::-1]

        n = len(s)
        resLen = 0
        ans = ""
        for i in range(n):
            for j in range(i+1,n+1):
                if isPalin(s[i:j]):
                    if j-i+1 > resLen:
                        ans = s[i:j]
                        resLen = j-i+1

        return ans