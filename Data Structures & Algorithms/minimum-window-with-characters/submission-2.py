class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or s == "" :
            return ""
        
        countT = Counter(t)
        window = {}
        need = len(countT)
        have = 0
        l = 0
        resLen = float("inf")
        ans = ""
        # the goal is to make sure their length and is equal and individual freq are equal
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and countT[c] == window[c]:
                have+=1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    ans = s[l:r+1]
            
                # shrink the window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        if ans:
            return ans
        
        return ""



