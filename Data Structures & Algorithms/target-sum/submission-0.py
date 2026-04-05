class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def rec(i,csum):
            if csum == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0

            return rec(i+1, nums[i]+csum) + rec(i+1,-nums[i] + csum)

        return rec(0,0) 