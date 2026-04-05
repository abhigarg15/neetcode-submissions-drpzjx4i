class Solution:
    def findMin(self, nums: List[int]) -> int:
        # high = len(nums)-1
        # low = 0
        # ans = nums[0]
        
        # while low <= high:
        #     if nums[low] < nums[high]:
        #         ans = min(nums[low], ans)
        #         return ans
            
            
        #     mid = low + (high - low)//2
        #     print(nums[high], nums[low], nums[mid])
        #     ans = min(nums[mid],ans)

        #     if nums[mid] >= nums[low]: # there is no target
        #         low = mid+1 
        #     else:
        #         high = mid-1

        
        # return ans
    
        """
        Using lower bound to find the solution
        """

        l = 0
        h = len(nums)-1

        while l < h:
            m = l + (h-l)//2

            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1

        return nums[l]
