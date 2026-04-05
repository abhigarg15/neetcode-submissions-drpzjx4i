class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        
        for i in range(len(nums)-k+1):
            maxVal = nums[i]
            for j in range(i,i+k):
                maxVal = max(nums[j],maxVal)
            
            output.append(maxVal)

        return output
