class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == "".join(reversed(s)):
            return True

        for i in range(len(s)):
            newTemp = s[:i] + s[i+1:]
            if newTemp == "".join(reversed(newTemp)):
                return True
        
        return False