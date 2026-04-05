class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = 0
        count = 0
        for num in nums:
            if count == 0:
                ans = num
                count+=1
            elif ans == num:
                count+=1
            else:
                count-=1

        return ans
                