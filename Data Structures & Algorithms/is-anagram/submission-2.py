class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Method 1: 
        sort the string element and check if there are equal, 
        TC = O(nlog(n))
        SC = O(1)
        """

        # return sorted(s) == sorted(t)

        """
        Method 2:
        we create a dictionary and store the frequency of the elements, decrement the frequency
        as we iterate through the next string, and check if all the values are 0

        TC = 0(3*n) = O(n)
        SC = O(n)
        """

        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1

        for i in t:
            if i not in freq:
                return False
            else:
                freq[i] = freq.get(i,0)-1
                if freq[i] < 0:
                    return False

        for key, value in freq.items():
            if value != 0:
                return False
        
        return True
        