class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        def rec(i):
            if i >= len(nums) - 1:
                return True
            ans = False
            for ni in range(1,nums[i]+1):
                ans |= rec(i+ni)

            return ans

        if not nums:
            return False
        return rec(0)