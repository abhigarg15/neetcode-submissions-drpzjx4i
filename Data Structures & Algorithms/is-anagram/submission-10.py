class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Method 1: 
        sort the string element and check if there are equal, 
        TC = O(nlog(n))
        SC = O(1)
        """

        # return sorted(s) == sorted(t) # no SC but TC

        """
        Method 2:
        we create a dictionary and store the frequency of the elements, decrement the frequency
        as we iterate through the next string, and check if all the values are 0

        TC = 0(3*n) = O(n)
        SC = O(n)
        """

        # return Counter(s) == Counter(t)
        # print(sorted(s))
        # print("".join(sorted(s)))
        # return sorted(s) == sorted(t)

        mp = Counter(s)

        for val in t:
            if val in mp and mp[val] > 0:
                mp[val] -= 1
            else:
                return False

        for val in mp.values():
            if val != 0:
                return False

        return True