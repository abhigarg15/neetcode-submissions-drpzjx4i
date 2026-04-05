class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            k = i+j
            ans = False
            if k == len(s3):
                return True
            if i < len(s1) and s1[i] == s3[k]:
                ans = ans or rec(i+1,j)
            
            if j < len(s2) and s2[j] == s3[k]:
                ans = ans or rec(i,j+1)

            dp[(i,j)] = ans
            return ans


        return rec(0,0)