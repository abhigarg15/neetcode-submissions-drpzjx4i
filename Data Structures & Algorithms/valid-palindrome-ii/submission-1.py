class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        This is a brute force approach
        """
        # if s == "".join(reversed(s)):
        #     return True

        # for i in range(len(s)):
        #     newTemp = s[:i] + s[i+1:]
        #     if newTemp == "".join(reversed(newTemp)):
        #         return True
        
        # return False

        """
        2 pointers
        """

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                skipL = s[left+1:right+1]
                skipR = s[left:right]

                return skipL == skipL[::-1] or skipR == skipR[::-1]

            
            left+=1
            right-=1

        
        return True



