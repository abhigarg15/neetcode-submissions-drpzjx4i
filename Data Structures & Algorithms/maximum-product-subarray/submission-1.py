class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        self.val = 0
        def rec (i,prev):
            if i == len(nums):
                return 
            
            self.val = max(self.val, prev*nums[i])
            rec(i+1, prev*nums[i])
            rec(i+1, 1)

        rec(0,1)
        
        return self.val