class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        res = 1
        track = set()
        while r < len(s):
            while s[r] in track:
                track.remove(s[l])
                l+=1 

            track.add(s[r])
            res = max(res,r-l+1)
            r+=1

        return res
