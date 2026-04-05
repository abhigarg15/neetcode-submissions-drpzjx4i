class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high - low) //2 

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1


        l = 0
        h = len(nums)-1

        while l <= h:
            mid = (l+h)//2

            if nums[mid] == target:
                return mid

            
            if nums[mid] < nums[h]:
                if nums[mid] < target:
                    l = mid+1
                else:
                    h = mid-1
            
            if nums[mid] > nums[h]:
                if target < nums[mid]:
                    l = mid+1
                else:
                    h = mid-1

        return -1











