class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        delta = (n*(n+1))//2 - sum(nums)
        return delta