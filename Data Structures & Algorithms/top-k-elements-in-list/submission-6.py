class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        Create Dictionary, store frequency of each element
        TC = O(n)
        SC = O(n)
        """

        d = {}

        for i in nums:
            d[i] = d.get(i,0)+1;

        ans = []
        # d = sorted(d, key = d.get, reverse= True) # this method returns the keys sorted by values
        d = sorted(d.items(), key = lambda item: item[1], reverse = True)
        for key,value in d:
            if k :
                ans.append(key)
                k-=1

        
        return ans