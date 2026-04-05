class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        if k > len(s2):
            return False

        r = 0
        while r+k <= len(s2):
            if sorted(s1) == sorted(s2[r:r+k]):
                return True
            r+=1
            # print(sorted(s1))
            # print(sorted(s2[r:r+k]))
        return False