class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0

        for i in range(len(s)):
            maxFrequency = 0
            d = {}
            for j in range(i,len(s)):
                d[s[j]] = d.get(s[j],0)+1
                maxFrequency = max(maxFrequency, d[s[j]])

                if (j - i + 1) - maxFrequency <= k:
                    ans = max(ans, j-i+1)

        return ans