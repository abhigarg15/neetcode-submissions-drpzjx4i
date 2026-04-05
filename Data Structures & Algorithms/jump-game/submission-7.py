class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # This has TC = n!        

        # def rec(i):
        #     if i >= len(nums) - 1:
        #         return True
        #     ans = False
        #     for ni in range(1,nums[i]+1):
        #         ans |= rec(i+ni)

        #     return ans

        # if not nums:
        #     return False
        # return rec(0)

        """
        We will try a greedy method approach
        """
        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0