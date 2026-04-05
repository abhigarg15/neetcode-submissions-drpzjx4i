class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        self.ans = 0
        def rec(i):
            if i == n:
                self.ans+=1
                return 

            if s[i] == "0":
                return
            
            rec(i+1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                rec(i+2)


        rec(0)
        return self.ans
