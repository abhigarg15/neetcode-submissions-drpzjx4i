class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Method 1: 
        sort the string element and check if there are equal, 
        TC = O(nlog(n))
        SC = O(1)
        """

        return sorted(s) == sorted(t)