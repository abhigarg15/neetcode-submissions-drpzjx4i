class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums = set(nums)
        ans = 1
        for num in nums:
            if num - 1 not in nums:
                temp = 1
                while num+temp in nums:
                    temp += 1
                
                ans = max(ans, temp)

        return ans