class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums)-1
        low = 0
        ans = nums[0]
        
        while low <= high:
            if nums[low] < nums[high]:
                ans = min(nums[low], ans)
                return ans
            
            
            mid = low + (high - low)//2

            ans = min(nums[mid],ans)

            if nums[mid] >= nums[low]: # there is no target
                low = mid+1
            else:
                high = mid-1

        
        return ans
    
