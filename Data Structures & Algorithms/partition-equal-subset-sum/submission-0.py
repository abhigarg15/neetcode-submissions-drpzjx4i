class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        target = sum(nums)//2

        def rec(i,sum1):

            if i >= len(nums) or sum1 > target:
                return False

            if sum1 == target:
                return True

            return rec(i+1,sum1+nums[i]) or rec(i+1,sum1)

        
        return rec(0,0)