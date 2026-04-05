class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = {}
        def rec(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + rec(i+1,j+1)
            else:
                dp[(i,j)] = max(rec(i,j+1), rec(i+1,j))

            return dp[(i,j)]


        return rec(0,0)

