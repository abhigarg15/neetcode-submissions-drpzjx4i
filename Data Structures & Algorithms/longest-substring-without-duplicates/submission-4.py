class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # mp = {}

        # l = 0

        # res = 0

        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l = max(mp[s[r]] + 1, l)
            
        #     mp[s[r]] = r
        #     res = max(res, r - l + 1)

        # return res

        l = 0
        r = 0
        length = 0
        tracker = set()
        while r < len(s):
            while s[r] in tracker:
                tracker.remove(s[l])
                l+=1

            tracker.add(s[r])

            length = max(length, r - l+1)
            r+=1

        return length

