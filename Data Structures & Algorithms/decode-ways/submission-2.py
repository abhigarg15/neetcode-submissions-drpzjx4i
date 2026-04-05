class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        self.ans = 0
        dp = defaultdict(int)
        def rec(i):
            if i == n:
                return 1

            if i in dp:
                return dp[i]

            res = rec(i+1)

            if s[i] == "0":
                return 0
            
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                res += rec(i+2)
            dp[i] = res
            return dp[i]

        return rec(0)
