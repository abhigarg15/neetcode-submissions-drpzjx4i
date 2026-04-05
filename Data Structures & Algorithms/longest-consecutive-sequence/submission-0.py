class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        store = set(nums) #storing it in set so that we dont find repeated numbers
        
        for num in nums:
            streak, curr = 0, num

            while curr in store: #till curr is in store
                streak+= 1
                curr += 1
            ans = max( ans, streak) # trying to find the max streak

        return ans