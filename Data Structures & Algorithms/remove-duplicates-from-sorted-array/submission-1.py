class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        cmp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != cmp:
                nums[idx] = nums[i]
                idx+=1
                cmp = nums[i]
        return idx