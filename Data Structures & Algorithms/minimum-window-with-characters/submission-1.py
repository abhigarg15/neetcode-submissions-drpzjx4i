class Solution:
    def minWindow(self, s: str, t: str) -> str:
        small = Counter(t)

        if len(t) > len(s) or t == "": 
            return ""

        have = 0
        need = len(small)
        res = [0,0]
        resLen = float("inf")
        l = 0
        window = {}

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in small and window[c] == small[c]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                window[s[l]]-=1
                if s[l] in small and window[s[l]] < small[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""






