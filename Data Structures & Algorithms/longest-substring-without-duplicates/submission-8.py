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

        # l = 0
        # r = 0
        # length = 0
        # tracker = set()
        # while r < len(s):
        #     while s[r] in tracker:
        #         tracker.remove(s[l])
        #         l+=1

        #     tracker.add(s[r])

        #     length = max(length, r - l+1)
        #     r+=1

        # return length
        # TC = O(n^2)
        # SC = O(n)
        if not s:
            return 0

        track = set()
        res = 1
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in track:
                    track.add(s[j])
                else:
                    res = max(res, len(track))
                    track = set()
                    break

        return res
                
            

            




