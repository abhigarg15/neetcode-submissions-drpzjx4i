class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(set(nums))
        ans = 1
        temp = 1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] - 1 == nums[i-1]:
                 temp += 1
            else:
                ans = max(ans, temp)
                temp = 1

        return max(ans,temp)