class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        def rec(i,prev):
            if i >= len(nums):
                return 0

            consider = 0
            if nums[i] > prev:
                consider = 1 + rec(i+1, nums[i])

            notconsider = rec(i+1,prev)
            return max(consider,notconsider)

    
        return rec(0, float("-inf"))